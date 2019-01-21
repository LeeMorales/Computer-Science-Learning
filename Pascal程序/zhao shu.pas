var
  a,s,b,i:longint;
begin
  read(a,b);
  for i:=1 to a do
   if i=b then s:=s+1;
  write(s);
end.