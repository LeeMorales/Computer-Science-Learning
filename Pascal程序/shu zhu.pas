var
  a:array[1..10] of real
  i:longint;
begin
  for i:=1 to 10 do
   read(a[i]);
  writeln;
  for i:=1 to 10 do
   if a[i] mod 2<>0 then
    write(a[i],' ');
  writeln;
   for i:=1 to 10
    if a[i] mod
