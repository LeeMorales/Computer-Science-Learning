var
  a,b,c,d,i,n:longint;
begin
  read(a,b);
  for i:=1 to a do begin
    d:=i;
    while d<>0 do begin
    c:=d mod 10;
    if b=c then n:=n+1;
    d:=d div 10;
    end;
  end;
  write(n);
end.
