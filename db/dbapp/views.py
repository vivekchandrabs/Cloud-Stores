from django.shortcuts import render,redirect,HttpResponse,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from dbapp.models import UserDetail,Store,Item,OrderShop,Order_Item,Cart
from django.core.mail import EmailMessage

from django.utils import timezone    
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from django.views.generic import View
from django.utils import timezone
from dbapp.render import Render
l=list()
		
li=list()
# Create your views here.
def signup(request):
	
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get("email")
		user_type=request.POST.get("user_type")
		user_type=int(user_type)
		print(user_type)
		address=request.POST.get("address")
		phone=request.POST.get("phone")
		
		try:
			user = User.objects.get(username=username)
			return render(request,'signup.html',{'show':'username already taken'})
			
		except:			
			user = User.objects.create_user(username, email, password)
		
			if user_type == 2:

				storeid=request.POST.get('storeid')
				print(storeid)
				no_of_stores=0
				
				profile=UserDetail(user=user,user_type=user_type,address=address,no_of_stores=no_of_stores,storeid=storeid,phone_no=phone)
				profile.save()
				return redirect('/signin/') 

			
				
				
			elif user_type ==1:
				no_of_stores=0
				storeid=0
				profile=UserDetail(user=user,user_type=user_type,no_of_stores=no_of_stores,storeid=storeid,address=address,phone_no=phone)
				profile.save()
				return redirect('/signin/') 

			
	try:				
		store=Store.objects.all()
		return render(request, "signup.html",{'store':store})
	except:
		
		return render(request, "signup.html",{'store':''})


def signin(request):
	user = request.user
	if user.is_authenticated:
		username=str(request.user)
		if user.userdetail.user_type == 1:
			url='/'+username+'/owner/'
			return redirect(url)
		else:
			storeid=user.userdetail.storeid
			storeid=str(storeid)
			url='/shop/'+storeid+'/checkout/'
			return redirect(url)

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, 
			password=password)
		if user is None:
			return render (request,'signin.html',{'caution':"User Name or Password Might be Wrong"})
		if user is not None:
			if user.userdetail.user_type == 1:
				login(request, user)
				username=request.user.username
				username=str(username)
				
				url='/'+username+'/owner/'
				return redirect(url)
			elif user.userdetail.user_type == 2 and user.username==username:
				login(request, user)
				username=request.user.username
				storeid=user.userdetail.storeid
				storeid=str(storeid)
				url='/shop/'+storeid+'/checkout/'
				return redirect(url)

			# return render(request,'additem.html')

	return render(request, "signin.html")

def Take_Text(request,user_name):

	if request.method=='POST':
		Text=request.POST.get('text')
		user=request.user
		user=User.objects.get(username=user)
		Take=Userdb(Text=Text,User=user)
		return HttpResponse('success')
	return render(request,'base.html')

def owner(request,owner):
	print(owner)
	user=request.user
	user=UserDetail.objects.get(user=user)
	storeofuser=Store.objects.filter(owner=user)

	return render(request,'owner.html',{'user_name':owner,'show':storeofuser})
	

def addstore(request,owner):
	print(owner)
	owner=request.user.username
	print('here in the addstore')
	if request.method=="POST":
		name=request.POST.get('storename')
		user=request.user
		user.userdetail.no_of_stores+=1
		user.userdetail.save()
		user=UserDetail.objects.get(user=user)
		print(type(user))

		store=Store(name=name,owner=user)
		store.save()
		# url='/'+owner+'/owner/'
		storeofuser=Store.objects.filter(owner=user)
		# return redirect(url)

		return render(request,'owner.html',{'user_name':owner,'show':storeofuser})
		# return HttpResponse("")
	return render(request,'addstore.html',{'user_name':owner})


def additem(request,storeid):
	owner=(request.user.username)
	user=request.user
	user=UserDetail.objects.get(user=user)
	user_type=user.user_type
	if request.method=="POST":
		name=request.POST.get('name')
		barcode=request.POST.get('barcode')
		quantity=request.POST.get('quantity')
		price=request.POST.get('price')

		store=Store.objects.get(pk=storeid)
		item=Item(name=name,barcode=barcode,quantity=quantity,price=price,store=store)
		item.save()

		store=Store.objects.get(pk=storeid)
		items=Item.objects.filter(store=store)
		print(type(items))
		return render(request,'additem.html',{'show':'','user_name':owner, "storeid":storeid,"showitem":items,"user_type":user_type})

		# storeitems=Item.objects.get(store__owner)
	
	return render(request,'additem.html',{'show':'','user_name':owner, "storeid":storeid,"user_type":user_type})

def viewitem(request,storeid):
	owner=request.user.username
	user=request.user
	
	try:
		store=Store.objects.get(pk=storeid)
		items=Item.objects.filter(store=store)
		user=request.user
		user=UserDetail.objects.get(user=user)
		user_type=user.user_type

		return render(request,'viewitems.html',{'showitem':items,'store':store,'storeid':storeid,'user_type':user_type,'user_name':owner,"user_type":user_type})
	except:
		return HttpResponse('no items in this store')

def chooseshop(request,storeid):#this is the page where owner can choose the shop
	storeid=str(storeid)
	user=request.user.username
	store=Store.objects.get(pk=storeid)
	try:
		shop=OrderShop.objects.filter(store=store)

		return render(request,"chooseshop.html",{'show':shop,'storeid':storeid,'user_name':user})
	except:
		return render(request,"chooseshop.html",{'show':'','storeid':storeid,"user_name":user})

def choosestore(request,owner):
	user=request.user
	user=UserDetail.objects.get(user=user)
	try:
		storeofuser=Store.objects.filter(owner=user)

		return render(request,'choosestore.html',{'user_name':owner,"show":''})
	except:
		return render(request,'choosestore.html',{'user_name':owner,"show":storeofuser})

def orderitems(request,storeid,shopid):#this is the page where the owner can enter the item details
	print("hello")
	owner=request.user.username
	if request.method=='POST':
		print("this is the method post")
		itemname=request.POST.get('itemname')
		quantity=request.POST.get('quantity')
		
		ordershop=OrderShop.objects.get(pk=shopid)
		shop=Order_Item(order_shop=ordershop,storeid=storeid,quantity=quantity,itemname=itemname)
		shop.save()
		name_shop=ordershop.name_shop
		address=ordershop.address
		email=ordershop.email
		shopkeeper=ordershop.shopkeeper_name
		phone=ordershop.phone_no
		storesname=ordershop.store.name
		message="Purchase order\n\
		store name: "+storesname+"\nshopkeeper name: "+shopkeeper+"\nphone:"+phone+"\n address:"+address+"\nitemname: "+itemname+"\nquantity: "+quantity+"\n  Thank you"
		print(message)
		print(email)
		msg = EmailMessage("Purchase Order", message, to=[email])
		msg.send()
		message="successfully ordered "+message
		return render(request,'orderitems.html',{'storeid':storeid,'shopid':shopid,"user_name":owner,"show":ordershop,"itemname":itemname,"quantity":quantity})

	return render(request,'orderitems.html',{'storeid':storeid,'shopid':shopid,"user_name":owner})


def addshop(request,storeid):
	owner=request.user.username
	if request.method=='POST':
		email=request.POST.get('email')
		storename=request.POST.get('storename')
		shopkeeper=request.POST.get('shopkeeper')
		phone=request.POST.get('phone')
		phone=int(phone)
		address=request.POST.get('address')

		store=Store.objects.get(pk=storeid)
		shop=OrderShop(store=store,name_shop=storename,address=address,email=email,shopkeeper_name=shopkeeper,phone_no=phone)
		shop.save()
		storeid=str(storeid)

		print(email)
		url='/'+storeid+'/chooseshop/'
		return redirect(url)
	print('here')
	return render(request,'addshop.html',{'storeid':storeid,"user_name":owner})

def deleteshop(request,owner):
	username=request.user.username
	user=request.user
	user=UserDetail.objects.get(user=user)
	try:
		storeofuser=Store.objects.filter(owner=user)
		return render(request,"delete.html",{"user_name":username,"show":storeofuser})
	except:
		return render(request,"delete.html",{"user_name":username,"show":''})

	

def deletestores(request,storeid):
	deletestore=Store.objects.get(pk=storeid)
	deletestore.delete()
	print("deleted")
	username=request.user.username
	url="/"+username+"/delete/"
	return redirect(url)

# def deletedistributer(request,shopid):
# 	deletedistributer=OrderShop.objects.get(pk=shopid)
# 	deletedistributer.delete()
# 	print("deleted")
# 	username=request.user.username
# 	url="/"+username+"/delete/"
# 	return redirect(url)
# def checkout(request,storeid):
# 	store=Store.objects.get(pk=storeid)
# 	user=request.user
# 	cart=Cart.objects.get(shopkeeper=user)
# 	email=request.POST.get('email')
# 	for i,k,

def customer(request,storeid):
	store=Store.objects.get(pk=storeid)
	user=request.user
	shopkeeper = UserDetail.objects.get(storeid=storeid,user=user, user_type=2)

	if request.user != shopkeeper.user:
		return redirect("/")
	
	cart=Cart.objects.get(shopkeeper=user)
	citems = cart.items
	cart={Item.objects.get(store=store, id=citem[0]):citem[1] for citem in citems}
	items = Item.objects.filter(store=store)
	if request.method=="POST":
		itemid=int(request.POST.get("itemname"))
		quantity=int(request.POST.get("quantity"))
		username=str(user)
		del l[:]
		l.append(itemid)
		l.append(quantity)
		try:
			del l[:]
			cart=Cart.objects.get(shopkeeper=username)
			l.append(itemid)
			l.append(quantity)
			cart.items.append(l)
			cart.save()



			print(cart.items)

			
		except:
			# items_dic={}
			# items_dic[itemid]=quantity
			del l[:]
			l.append(itemid)
			l.append(quantity)
			


			cart=Cart(shopkeeper=username,items=[])
			cart.save()
			print(cart.items)
			cart=Cart.objects.get(shopkeeper=username)
			cart.items.append(l)
			cart.save()
			print(cart.items)
	


	


	return render(request,"customer.html",{'items':items,'storeid':storeid, "cart":cart})


def generate_pdf(pk):
	y = 700
	buffer = BytesIO()
	p = canvas.Canvas(buffer, pagesize=letter)
	p.setFont('Helvetica', 10)
	k=""
	j=k.join(pk)
	p.drawString(220, y, j)
	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()
	return pdf


def sendemail(request):
	username=request.user.username
	cart=Cart.objects.get(shopkeeper=username)
	pk=cart.items
	# pk="message in the pdf"
	sales=1
	today = timezone.now()
	params = {
	'today': today,
	'sales': sales,
	'request': request
				}
	pdf=Render.render('pdf.html', params)

	# pdf = generate_pdf(pk)
	msg = EmailMessage("title", "content", to=["vivek.dexter.301096@gmail.com"])
	msg.attach('my_pdf.pdf', pdf, 'application/pdf')
	msg.content_subtype = "html"
	msg.send()
	

	# message="this is the message of the django email"
	# Subject="this is the Subject"
	# email = EmailMessage(Subject,message, to=['vivek.dexter.301096@gmail.com'])
	# fd = open('NS.pdf', 'rb')
	# email.attach('NS.pdf', pdf, 'application/pdf')
   
	# res = email.send()
	
	# email.send()
	return HttpResponse("success")


# def get() request):
#        sales="the"
#        today = timezone.now()
#        params = {
#             'today': today,
#             'sales': sales,
#             'request': request
#         }
#         return Render.render('pdf.html', params)

def signout(request):
	user = request.user
	logout(request)
	return redirect('/')