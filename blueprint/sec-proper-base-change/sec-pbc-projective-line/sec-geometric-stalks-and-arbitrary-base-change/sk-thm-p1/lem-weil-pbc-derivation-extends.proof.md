+++
kind = "proof"
of = "lem-weil-pbc-derivation-extends"
+++
($D(1)=0$.) $D(1)=D(1\cdot1)=1\cdot D(1)+1\cdot D(1)=2D(1)$, so $D(1)=0$. The same computation shows $\delta(1)=0$ for every derivation $\delta$ of any commutative ring.

($D(I^{n+1})\subseteq I^n$ for $n\geq0$.) Induction on $n$. For $n=0$, $I^0=R$. Let $n\geq1$ and assume $D(I^n)\subseteq I^{n-1}$. The ideal $I^{n+1}$ consists of finite sums of products $xy$ with $x\in I$, $y\in I^n$. For such a product $D(xy)=xD(y)+yD(x)$ with $xD(y)\in I\cdot I^{n-1}=I^n$ and $yD(x)\in I^n$; since $D$ is additive, $D(I^{n+1})\subseteq I^n$. (This is the source's '$D(I^n)\subset I^{n-1}$ by the Leibniz rule', with the index shifted by one.)

(The maps $D_n$.) For $n\geq1$ let $p_n:R/I^{n+1}\to R/I^n$ be the reduction map. By the previous step $D_n:R/I^{n+1}\to R/I^n$, $a\bmod I^{n+1}\mapsto D(a)\bmod I^n$, is well defined: if $a-a'\in I^{n+1}$ then $D(a)-D(a')=D(a-a')\in I^n$. It is additive, and for $s=a\bmod I^{n+1}$, $t=b\bmod I^{n+1}$ we have $D_n(st)=D(ab)\bmod I^n=p_n(s)D_n(t)+p_n(t)D_n(s)$. For $n\geq2$ the $D_n$ commute with the reductions: $p_{n-1}(D_n(a\bmod I^{n+1}))=D(a)\bmod I^{n-1}=D_{n-1}(p_n(a\bmod I^{n+1}))$.

(Definition of $D^\wedge$.) By definition of the $I$-adic completion, an element of $R^\wedge$ is a sequence $x=(x_n)_{n\geq1}$, $x_n\in R/I^n$, with $p_n(x_{n+1})=x_n$, and the ring operations are componentwise. For such $x$ put $D^\wedge(x)=(D_n(x_{n+1}))_{n\geq1}$. This is again a compatible sequence: $p_{n-1}(D_n(x_{n+1}))=D_{n-1}(p_n(x_{n+1}))=D_{n-1}(x_n)$ by the previous step. So $D^\wedge:R^\wedge\to R^\wedge$ is a map (the limit of the $D_n$, as in the source).

($D^\wedge$ is a derivation; the source omits this verification.) Additivity holds componentwise since each $D_n$ is additive. For $x,y\in R^\wedge$ the $n$-th component of $D^\wedge(xy)$ is $D_n(x_{n+1}y_{n+1})=p_n(x_{n+1})D_n(y_{n+1})+p_n(y_{n+1})D_n(x_{n+1})=x_nD_n(y_{n+1})+y_nD_n(x_{n+1})$ (step 3), which is the $n$-th component of $xD^\wedge(y)+yD^\wedge(x)$, the operations of $R^\wedge$ being componentwise.

($D^\wedge\circ c=c\circ D$.) For $a\in R$, $c(a)=(a\bmod I^n)_{n\geq1}$ by definition of the completion map, so the $n$-th component of $D^\wedge(c(a))$ is $D_n(a\bmod I^{n+1})=D(a)\bmod I^n$, the $n$-th component of $c(D(a))$. This proves (1).

((2), uniqueness.) Let $\delta:W^{-1}R\to W^{-1}R$ be a derivation with $\delta\circ\lambda=\lambda\circ D$. For $w\in W$, $\lambda(w)\cdot(1/w)=1$, so by step 1 (applied to $\delta$) and the Leibniz rule $0=\delta(1)=\lambda(w)\delta(1/w)+(1/w)\lambda(D(w))$; multiplying by $1/w$ gives $\delta(1/w)=-D(w)/w^2$. Then $a/w=\lambda(a)\cdot(1/w)$ gives $\delta(a/w)=\lambda(a)\delta(1/w)+(1/w)\lambda(D(a))=D(a)/w-aD(w)/w^2$. So $\delta$ is determined by $D$ and is given by the stated formula.

((2), well defined.) Put $\delta(a,w)=(D(a)w-aD(w))/w^2\in W^{-1}R$ for $a\in R$, $w\in W$; it equals $D(a)/w-aD(w)/w^2$. Suppose $a/w=a'/w'$, i.e. $u z=0$ for some $u\in W$, where $z=aw'-a'w$. Applying $D$ to $uz=0$ gives $D(u)z+uD(z)=0$; multiplying by $u$ and using $uz=0$ gives $u^2D(z)=0$. Now put $E=D(a)ww'^2-aD(w)w'^2-D(a')w'w^2+a'D(w')w^2$, so that $\delta(a,w)-\delta(a',w')=E/(ww')^2$. Expanding $D(z)=D(a)w'+aD(w')-D(a')w-a'D(w)$ and $D(ww')=D(w)w'+wD(w')$ one checks $E=ww'D(z)-zD(ww')$. Hence $u^2E=ww'\cdot u^2D(z)-D(ww')\cdot u\cdot uz=0$ with $u^2\in W$, so $E/(ww')^2=0$ in $W^{-1}R$ and $\delta(a,w)=\delta(a',w')$. Thus $D_W(a/w):=\delta(a,w)$ is a well defined map $W^{-1}R\to W^{-1}R$.

((2), additive.) $a/w+b/v=(av+bw)/wv$, and with $D(av+bw)=D(a)v+aD(v)+D(b)w+bD(w)$, $D(wv)=D(w)v+wD(v)$ the numerator of $\delta(av+bw,wv)$ is $wv\,D(av+bw)-(av+bw)D(wv)=v^2(D(a)w-aD(w))+w^2(D(b)v-bD(v))$, so $\delta(av+bw,wv)=\delta(a,w)+\delta(b,v)$, i.e. $D_W(a/w+b/v)=D_W(a/w)+D_W(b/v)$.

((2), Leibniz rule.) $(a/w)(b/v)=ab/wv$ and $D_W(ab/wv)=\big((aD(b)+bD(a))wv-ab(D(w)v+wD(v))\big)/w^2v^2$, while $(a/w)D_W(b/v)+(b/v)D_W(a/w)=\big(aw(D(b)v-bD(v))+bv(D(a)w-aD(w))\big)/w^2v^2$; both numerators equal $aD(b)wv+bD(a)wv-abwD(v)-abvD(w)$. So $D_W$ is a derivation.

((2), extension.) $D_W(\lambda(a))=D_W(a/1)=(D(a)\cdot1-aD(1))/1=\lambda(D(a))$ by step 1. With steps 7 to 10 this proves (2).
