+++
kind  = "proof"
of    = "sk-prop-sf-localization"
+++
*The vanishing.* By $Lj^*\dashv Rj_*$,
$\operatorname{Hom}((Ri_!B)[n],Rj_*C)\cong\operatorname{Hom}((Lj^*Ri_!B)[n],C)$,
and $Lj^*Ri_!=0$ by base change of $Ri_!$ along $j$, the fibre product
$Z\times_XU$ being empty.

*Existence.* First, for every $M\in D(X_{\Et},\mathcal A)$, represented by a
complex of sheaves, the functors $j^*$, $j_!$, $i^*$, $i_*$ are exact, so
applying the short exact sequence of [sk-prop-sf-open-closed-triangle]
termwise gives a short exact sequence of complexes
$0\to j_!j^*M\to M\to i_*i^*M\to0$, hence a distinguished triangle
$j_!j^*M\to M\to Ri_*i^*M\xrightarrow{+1}$. In particular, if $j^*M=0$ then
$M\cong Ri_*i^*M$.

Complete the counit to a distinguished triangle
$Ri_!Ri^!L\xrightarrow{\varepsilon_L}L\xrightarrow{u}C\xrightarrow{w}
Ri_!Ri^!L[1]$. Apply $Lj^*$: as $Lj^*Ri_!=0$, $Lj^*u$ is an isomorphism
$Lj^*L\cong Lj^*C$. Apply $Ri^!$: by [sk-prop-sf-closed-unit] the unit
$Q\to Ri^!Ri_!Q$ is an isomorphism, so by the triangle identity
$Ri^!\varepsilon_L$ is an isomorphism and $Ri^!C=0$.

Now let $D$ be the cone of the unit $C\to Rj_*Lj^*C$. Since $j$ is an open
immersion, $Lj^*Rj_*\cong\mathrm{id}$ via the counit, so $Lj^*D=0$; and
$Ri^!Rj_*=0$, because
$\operatorname{Hom}(B,Ri^!Rj_*C')\cong\operatorname{Hom}(Ri_!B,Rj_*C')=0$ for
all $B$ by the vanishing above, so $Ri^!D=0$ as $Ri^!C=0$. From $Lj^*D=0$ we
get $D\cong Ri_*i^*D$, whence $i^*D\cong Ri^!Ri_!i^*D\cong Ri^!D=0$ by
[sk-prop-sf-closed-unit] again, and $D=0$. So $C\to Rj_*Lj^*C$ is an
isomorphism, and composing with $Rj_*Lj^*u^{-1}$ gives an isomorphism
$\varphi:C\xrightarrow{\sim}Rj_*Lj^*L$ with $\varphi\circ u=\eta_L$, by
naturality of the unit. Transporting the triangle along $\varphi$, i.e.
setting $\delta_L=w\circ\varphi^{-1}$, gives a distinguished triangle
$(\varepsilon_L,\eta_L,\delta_L)$.

*Uniqueness and naturality.* Let $f:L\to L'$ and suppose given distinguished
triangles of the stated form on $L$ and on $L'$ (with any connecting maps).
Since
$\eta_{L'}\circ f\circ\varepsilon_L=\eta_{L'}\circ\varepsilon_{L'}\circ
Ri_!Ri^!f=0$, the axioms of a triangulated category give a morphism of triangles with middle component $f$.
Two maps $Rj_*Lj^*L\to Rj_*Lj^*L'$ agreeing after composition with
$\eta_L$ differ by a map factoring through $\delta_L$, hence through an
element of $\operatorname{Hom}(Ri_!Ri^!L[1],Rj_*Lj^*L')=0$; dually on the first
vertex. So a morphism between these triangles is determined by its middle
component, and the one extending $f$ must be $(Ri_!Ri^!f,f,Rj_*Lj^*f)$, as
these components commute with $\varepsilon$ and $\eta$ by naturality. For
$L=L'$, $f=\mathrm{id}$ and two choices $\delta_L$, $\delta'_L$ of connecting
map, the morphism of triangles is $(\mathrm{id},\mathrm{id},\mathrm{id})$, and
compatibility with the connecting maps gives $\delta_L=\delta'_L$ (BBD,
1.1.9–1.1.10).

Source: open–closed localization in SGA 4, XVII–XVIII; used in SGA 5, III,
proof of 1.7.4.
