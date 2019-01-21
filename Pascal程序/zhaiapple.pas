var
  a,b:array[1..10] of integer;
  x,i,s,n:integer;
begin
  read(x);
  for i:=1 to 10 do
  begin
    read(a[i]);
    if x+30      >a[i] then s:=s+1;
  end;
  write(s);
end.
