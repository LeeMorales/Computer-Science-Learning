var
  a,b,c,x,y,z:longint;
begin
  for a:=1 to 1000000 do
   for b:=1 to 1000000 do
    for c:=1 to 1000000 do
     if a-2+b+2+c*2=30 then write(a,'       ',b,'       ',c);
end.
