var
  s,t,i,m,n:longint;
  a,b:text;
begin
  assign(a,'calcultain.in');
  reset(a);
  assign(b,'calcultain.out');
  rewrite(b);
   read(a,s,i,t);
   m:=2*(i*s+i*t+s*t);
   n:=s*i*t;
   writeln(b,m);
   writeln(b,n);
   close(a);
   close(b);
end.



