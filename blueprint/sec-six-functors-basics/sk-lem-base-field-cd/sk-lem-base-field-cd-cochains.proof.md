+++
kind = "proof"
of = "det-base-field-cd-cochains"
+++
A continuous map from the compact space $G^s$ to a discrete set is locally
constant with finite image, and is constant on the cosets of $N^s$ for some open
normal subgroup $N$.

*(1).* If $0\to M'\to M\to M''\to0$ is exact in $\mathcal C_G$, then
$0\to C^s(G,M')\to C^s(G,M)\to C^s(G,M'')\to0$ is exact: injectivity and
exactness in the middle are clear, and a continuous cochain with values in
$M''$ takes finitely many values on finitely many clopen pieces, each of which
can be lifted to $M$, giving a continuous lift. The long exact cohomology
sequences make $H^\bullet(C^\bullet(G,-))$ a $\delta$-functor, and
$H^0=M^G$.

Effaceability: let $I=\operatorname{Map}_{\mathrm{cont}}(G,M)$ with
$(hf)(g)=f(gh)$. A locally constant $f$ is constant on the cosets $gN$ for some
open normal $N$, so $hf=f$ for $h\in N$; thus $I\in\mathcal C_G$. The map
$m\mapsto\varphi_m$, $\varphi_m(g)=gm$, is equivariant
($(h\varphi_m)(g)=ghm=\varphi_{hm}(g)$) and injective ($\varphi_m(1)=m$). Use
homogeneous cochains, i.e. equivariant continuous $F\colon G^{r+1}\to I$, which
compute the same cohomology as inhomogeneous ones by the usual change of
variables. Such $F$ correspond bijectively to arbitrary continuous
$f\colon G^{r+1}\to M$ via $f(g_0,\dots,g_r)=F(g_0,\dots,g_r)(1)$ and
$F(g_0,\dots,g_r)(t)=f(tg_0,\dots,tg_r)$, compatibly with the alternating-sum
differentials. On the complex of all continuous $f$, the operator
$(hf)(g_0,\dots,g_{r-1})=f(1,g_0,\dots,g_{r-1})$ satisfies $dh+hd=\mathrm{id}$ in
positive degrees, so $H^s(G,I)=0$ for $s>0$. An effaceable $\delta$-functor is
universal (Stacks Project, Tag 010T); the right derived functors of invariants
form a universal $\delta$-functor with the same $H^0$, so the two agree.

*(2).* A continuous cochain has finite image, which lies in some $M_\alpha$;
hence $C^\bullet(G,M)=\varinjlim_\alpha C^\bullet(G,M_\alpha)$, and cohomology
commutes with filtered colimits of complexes of abelian groups.

*(3).* By the first remark every continuous cochain on $G^s$ factors through
$(G/N)^s$ for some open normal $N$, which may be shrunk to act trivially on $M$;
the transition maps are inflations, i.e. pullback of cochains. Cohomology
commutes with the filtered colimit.
