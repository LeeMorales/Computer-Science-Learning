var
  n,m,i,s:longint;
begin
  writeln('please write two number');
  read(m,n);
  i:=1;
  s:=m*i;
  while s mod n<>0 do
    begin
      i:=i+1;
      s:=m*i;
    end;
    writeln('m and n de zui xiao gong bei shu shi',' ',s);
end.
