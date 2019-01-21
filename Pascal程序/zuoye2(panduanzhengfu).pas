var
  i,n,x,y,z:longint;
begin
  x:=0;
  y:=0;
  z:=0;
  for i:=1 to 30 do
    begin
      read(n);
      if n>0 then x:=x+1;
      if n<0 then y:=y+1;
      if n=0 then z:=z+1;
    end;
  writeln(x,y,z);
end.
