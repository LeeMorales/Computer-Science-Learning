var
 a,b:array[1..5] of longint;
 i,j,n,q,l:longint;
 t,k,y,x:longint;
begin
  read(n);
  for i:=1 to n do
  begin
   read(q);
   if q mod 2=0 then
                  begin
                    k:=k+1;
                    b[k]:=q;
                  end
                else begin
                       l:=l+1;
                       a[l]:=q;
                     end;
                  end;
for j:=1 to 10 do
     if a[i]<a[j] then
      begin
        t:=a[i];
        a[i]:=a[j];
        a[j]:=t;
      end;
  for i:=1 to 5 do
    write(a[j],' ');

end.
