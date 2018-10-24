var
  n,m,b,s:longint;
begin
  read(m,n);
  b:=1;
  s:=m div b;
  while n mod s<>0 do
   begin
     b:=b+1;
     s:=m div b;
   end;
  writeln('m and n de zui da gong yin shu shi',' ',s);
end.
