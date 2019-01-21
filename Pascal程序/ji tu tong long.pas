var
 m,n:longint;
begin
  for m:=1 to 27 do
   for n:=1 to 27 do
     if m+n=27 then
       if 4*m+2*n=82 then  writeln('sheep',m,'chicken',n);
end.