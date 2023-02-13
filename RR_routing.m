clc;
clear all;
 
C1_old = [0 0.025 0.0906 0.1066 0.1078 0.086 0.039 0.027 0.017 0.0123 0.0074 0.0025 0];
t1_old = [6.5 7 7.5 8 8.5 9 10 10.5 11 11.5 12 13 14];


C2 = [0 0.0027 0.0108 0.0285 0.0514 0.066 0.0753 0.087 0.0712 0.0492 0.0372 0.0305 0.0223 0.0102 0.0053 0.00325 0.00107 0.0016 0];
t2 = [13.5 14 14.5 15 15.5 16 16.5 17 18 18.5 19 19.5 20 21 22 23 24 25 28];

u = numel(C2) 

%interpolation
for i = 1:1:16
n= 6 + (i/2);
t1(i) = n;    
C1(i)=interp1(t1_old,C1_old,n);
end 
t1          % Time 6.5 to 14
C1          % Concentration from t = 6.5 to 14



 
t2_bar =  17.78;
t1_bar = 8.79;

dell_tau = 0.5; 
E = 0.029;    
U = 0.7;   
CD = sqrt(4*3.14*E*(t2_bar -t1_bar));
BC = 4*E*(t2_bar-t1_bar);

p = numel(t2);
q = numel(t1);
q = q-1;
for j = 1:p
    t = (t2(j));
    
for i = 1:1:q
tau = t1(i);        
                                                                                  %t = 60*(i*3);
AB = -((U*(t2_bar - t1_bar - t + tau))^2);
DE = (exp(AB/BC))/CD;
l(i) =(U*C1(i+1)*DE*dell_tau);
end
C3(j) = sum(l);
end
C3          % estimated concentration
r = numel(C3); 
% to calculate D
D1 = C3-C2;
D2 = D1.^2;
D = sum(D2)/r

plot(t2,C3,'-r');            % red graph is estimated one
hold on;
plot(t2,C2,'-b');           % blue graph is observed one


