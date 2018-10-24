var
  a,b,c,s:longint;
begin
  for a:=1 to 33 do
  for b:=1 to 48 do
  for c:=1 to 100 do
  if(a+b+c=100) and (3*a+2*b+c/3=100)then
begin
  writeln(a,' ',b,' ',c);s:=s+1;
end;
write('s=',s);
end.
