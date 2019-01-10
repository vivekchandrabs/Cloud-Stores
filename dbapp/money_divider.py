import time

class money1:
	l=[1,2,5,10,20,50,100,200,500,2000]
	sum1=0
	
	num=[]
	t=0
	d={}
	
	val=2000
	ex=[]
	re=0
	h=0
	q=0


	def fill(self,sum1):
		self.sum1=(sum1)
		


	

	def clc(self,t):
		while (sum(self.num)!=self.sum1):

			max_num=max(self.l)
				# print(max_num)
			diff=t-max_num
			if diff<0:
					
				
				self.l.remove(max_num)
			else:
				
				self.num.append(max_num)
					#l.remove(max_num)

			if diff in self.l:
				self.num.append(diff)
					# print(num)
			else:
				if diff<0:
					pass
				else:
					
					diff=abs(diff)
					# print(diff)
					t=diff



	def go(self):
		

		while (sum(self.num)!=self.sum1):
			
			
			if (self.sum1>=2000):
				if self.sum1%self.val==0:
					while self.sum1%self.val==0:
						f=int(self.sum1/self.val)
						
						if self.val*f==self.sum1:
							self.g=int(self.val/2000)
							
							self.h=int(self.g*f)			

						self.val=int(self.val*10)
					self.ex.append(2000)
					self.ex=self.ex*self.h
					
					self.num.extend(self.ex)

				else :
					
					while ((self.sum1-self.t)%2000!=0):
						
						self.t=self.sum1%self.val
						self.q=self.sum1-self.t
						self.val=self.val*10
					

					self.val=2000

					while self.q%self.val==0:
						
						f=int(self.q/self.val)
							
						if self.val*f==self.q:
							self.g=(self.val/2000)
								
							self.h=int(self.g*f)			

						self.val=(self.val*10)
					self.ex.append(2000)
					self.ex=self.ex*self.h
					
						
					self.num.extend(self.ex)
					self.clc(self.t)
					

			else:
				

				self.clc(self.sum1)
		

	def printing(self):
		for i in self.num:
			if i in self.d:
				self.d[i]+=1
			else:
				self.d[i]=1
		
		
		print(self.d)
		return self.d

	def refill(self):

		self.sum1=0
		self.d.clear()
		del self.num[:]
		self.t=0
		self.l=[1,2,5,10,20,50,100,200,500,2000]
		self.val=2000
		del self.ex[:]
		self.re=0
		self.h=0
		self.q=0
	
		
		

		


			


		
		

