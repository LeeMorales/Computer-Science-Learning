var
  i,l,a,b,c,d:longint;
begin
  for i:=1000 to 9999 do
  begin
    a:=i div 1000;
    b:=i div 100 mod 10;
    c:=i div 10 mod 10;
    d:=i mod 10;
    if((i mod 3)or(i mod 5)=2)
    and((a=2)or(a=3)or(a=5)or(a=7)or(a=9))
    and((b=2)or(b=3)or(b=5)or(b=7)or(b=9))
    and((c=2)or(c=3)or(c=5)or(c=7)or(c=9))
    and((d=2)or(d=3)or(d=5)or(d=7)or(d=9))then
    writeln(a,b,c,d);
  end;
end.