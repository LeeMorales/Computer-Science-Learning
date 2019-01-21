var
  i,n,a,b,c:longint;
begin
  read(n);
  a:=n div 100;
  c:=n mod 10;
  if a=c then write('hui wen shu')
         else writeln('e.......');
end.
