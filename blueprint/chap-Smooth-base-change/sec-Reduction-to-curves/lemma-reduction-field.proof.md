+++
kind = "proof"
of = "lemma-reduction-field"
order = 676
uses = ["definition-small-pro-etale-site", "definition-underived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "lemma-injectivity-base-change-map-degree", "lemma-schematic-closure-uniqueness"]
+++
We shrink the source of the direct image, keeping a fixed
nonzero element of the cokernel, until it becomes the spectrum of a field. A
minimal closed subscheme carrying the failure exists by a limit argument,
and its generic point still carries it. The one nonformal step is the
third property below, which says that a failure on a scheme is seen either
on an open subscheme or on its closed complement, and whose proof uses the
injectivity of the base change map.

We first fix notation for the cokernels. Let $T$ be a $Y$-scheme, put
$T'=Y'\times_YT$, and let $g_T:T'\to T$ be the projection. For a qcqs
morphism $h:Z'\to T$ we write $h':Z'_{T'}=Z'\times_TT'\to T'$ and
$g_{Z'}:Z'_{T'}\to Z'$ for its base changes, and for a sheaf $N$ of
$\mathbf Z/n$-modules on $Z'_{\acute{e}t}$ we put

$$
b^q_{h,N}:g_T^{-1}R^qh_*N\longrightarrow R^qh'_*g_{Z'}^{-1}N,
\qquad
C(h,N)=\operatorname{coker}\bigl(b^q_{h,N}\bigr),
$$

a sheaf on $T'_{\acute{e}t}$. These cokernels are functorial in two ways. A map of
sheaves $N\to N_1$ on $Z'_{\acute{e}t}$ induces $C(h,N)\to C(h,N_1)$, and a morphism
$u:Z''\to Z'$ induces $C(h,N)\to C(hu,u^{-1}N)$, by pulling back along $u$:
upstairs through $N\to u_*u^{-1}N$ and the edge map
$R^qh_*u_*\to R^q(hu)_*$, and downstairs in the same way. These pullback maps
are compatible with the base change maps, and with composition in $u$,
because base change maps compose [Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)].

Since $\mathrm{BC}(g,n,q)$ fails, there are a $Y$-scheme $T$, a qcqs morphism
$f:Z\to T$ and a sheaf $M$ of $\mathbf Z/n$-modules on $Z_{\acute{e}t}$ such that
$b^q_{f,M}$ is not an isomorphism. By
Lemma [lemma-injectivity-base-change-map-degree] it is injective, so
$C(f,M)\neq0$, and we fix a geometric point $\bar t'$ of $T'$ and a nonzero
element $\xi\in C(f,M)_{\bar t'}$. For a qcqs morphism $u:Z'\to Z$ let
$P(Z')$ mean that the image $\xi_{Z'}$ of $\xi$ in
$C(fu,u^{-1}M)_{\bar t'}$ is nonzero. The verification in [Stacks, [0F07](https://stacks.math.columbia.edu/tag/0F07)]
shows that $P$ has three properties.

1. thickenings preserve $P$, by topological invariance;
2. limits with affine transition maps preserve $P$, by continuity;
3. if $P(Z')$ holds and $V\subset Z'$ is a quasi-compact open with
   closed complement $W$, then $P(V)$ or $P(W)$ holds.

To prove the third property, write $h=fu:Z'\to T$ and $M'=u^{-1}M$, and let
$j:V\to Z'$ and $i:W\to Z'$ be the inclusions. We split $M'$ into an open
part and a closed part. Choose an injective sheaf $J$ of
$\mathbf Z/n$-modules on $V_{\acute{e}t}$ containing $j^{-1}M'$. Then the map

$$
M'\longrightarrow j_*J\oplus i_*i^{-1}M',
$$

whose components are adjoint to $j^{-1}M'\subset J$ and to the identity of
$i^{-1}M'$, is injective. Indeed, at a geometric point of $V$ its first
component is the inclusion $M'_{\bar v}\subset J_{\bar v}$, and at a
geometric point of $W$ its second component is the identity of
$M'_{\bar w}$. By the second assertion of
Lemma [lemma-injectivity-base-change-map-degree], the induced map

$$
C(h,M')\longrightarrow C(h,j_*J)\oplus C(h,i_*i^{-1}M')
$$

is injective as well. Since $P(Z')$ holds, $\xi_{Z'}\neq0$, and therefore its
image in $C(h,j_*J)_{\bar t'}$ or its image in $C(h,i_*i^{-1}M')_{\bar t'}$
is nonzero. We show that the second case gives $P(W)$ and the first gives
$P(V)$.

The closed summand is formal. The base change $i':W_{T'}\to Z'_{T'}$ of $i$
is again a closed immersion, and closed direct images are exact and commute
with every base change (Lemma [lemma-finite-morphisms]). Hence, for a
sheaf $N$ on $W_{\acute{e}t}$,

$$
R^qh_*(i_*N)=R^q(hi)_*N,
\qquad
R^qh'_*\bigl(g_{Z'}^{-1}i_*N\bigr)=R^qh'_*\bigl(i'_*g_W^{-1}N\bigr)
=R^q(hi)'_*g_W^{-1}N,
$$

and these identifications are compatible with the base change maps
[Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)]. Thus
$C(h,i_*N)=C(hi,N)$. For $N=i^{-1}M'$ the image of $\xi_{Z'}$ in
$C(h,i_*i^{-1}M')_{\bar t'}$ becomes $\xi_W$, and so it is nonzero exactly when
$P(W)$ holds.

The open summand needs the induction hypothesis, because $j$ is not finite.
Let $j':V_{T'}\to Z'_{T'}$ and $g_V:V_{T'}\to V$ be the base changes of $j$,
and compare the Leray spectral sequences for $hj=h\circ j$ and
$h'j'=h'\circ j'$. Upstairs, $R^bj_*J=0$ for $b>0$ because $J$ is injective,
so the Leray spectral sequence collapses and gives

$$
R^qh_*(j_*J)\xrightarrow{\ \sim\ }R^q(hj)_*J .
$$

Downstairs we use $\mathrm{BC}(g,n,q-1)$. The scheme $Z'$ is a $Y$-scheme
through $T$, and $Z'_{T'}=Y'\times_YZ'$, so the square formed by $j$, $j'$,
$g_{Z'}$ and $g_V$ is one of the squares in the definition of $\mathrm{BC}$.
Hence

$$
g_{Z'}^{-1}R^bj_*J\xrightarrow{\ \sim\ }R^bj'_*g_V^{-1}J
\qquad(0\le b\le q-1).
$$

For $b=0$ this identifies $g_{Z'}^{-1}j_*J$ with $j'_*g_V^{-1}J$, and for
$0<b<q$ it shows that $R^bj'_*g_V^{-1}J=0$. Consequently, in the Leray
spectral sequence

$$
E_2^{a,b}=R^ah'_*R^bj'_*g_V^{-1}J\ \Longrightarrow\
R^{a+b}(h'j')_*g_V^{-1}J
$$

the rows $0<b<q$ vanish. No differential can reach $E^{q,0}$: the
differential $d_r$ into $E_r^{q,0}$ starts at $E_r^{q-r,r-1}$, which is zero
for $2\le r\le q$ because then $0<r-1<q$, and for $r>q$ because then
$q-r<0$. So $E_2^{q,0}=E_\infty^{q,0}$, which is the bottom step of the
filtration of the abutment, and the edge map

$$
e:R^qh'_*\bigl(j'_*g_V^{-1}J\bigr)\longrightarrow R^q(h'j')_*g_V^{-1}J
$$

is injective. Since base change maps compose [Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)] and edge
maps are natural, the square

$$
\begin{CD}
g_T^{-1}R^qh_*(j_*J) @>{b^q_{h,j_*J}}>> R^qh'_*\bigl(j'_*g_V^{-1}J\bigr)\\
@V{\wr}VV @VV{e}V\\
g_T^{-1}R^q(hj)_*J @>{b^q_{hj,J}}>> R^q(h'j')_*g_V^{-1}J
\end{CD}
$$

commutes. Its left arrow is an isomorphism and its right arrow is injective,
so it induces an injective map $C(h,j_*J)\to C(hj,J)$. (In the top row we
have identified $g_{Z'}^{-1}j_*J$ with $j'_*g_V^{-1}J$ by the case $b=0$; this
does not change the cokernel.) The vertical arrows are the pullback maps
along $j$, so this map is pullback along $j$ followed by $j^{-1}j_*J=J$.

It remains to pass from $J$ back to $j^{-1}M'$. By naturality, the composite
$C(h,M')\to C(h,j_*J)\to C(hj,J)$ equals the composite
$C(h,M')\to C(hj,j^{-1}M')\to C(hj,J)$ of pullback along $j$ and the map
induced by $j^{-1}M'\subset J$. In the first case the image of $\xi_{Z'}$ in
$C(h,j_*J)_{\bar t'}$ is nonzero, hence so is its image in
$C(hj,J)_{\bar t'}$. This image is the image of $\xi_V$ under the second
composite, and so $\xi_V\neq0$, which is $P(V)$.

The field comes out of the three properties as follows. The intersection
of a decreasing chain of closed subschemes is the limit of the chain, with
affine transition maps. By the second property and Zorn's lemma there is
therefore a minimal closed subscheme with $P$. It is nonempty, since $P$
fails for the empty scheme, and by the first property it is reduced. Let
$\xi$ be the generic point of an irreducible component. We claim that every
affine open neighbourhood of $\xi$ has $P$. Indeed, by the third property,
either the neighbourhood or its closed complement has $P$, and the
complement is a closed subscheme not containing $\xi$, hence strictly
smaller, so by minimality it does not have $P$. Since the minimal closed
subscheme is reduced, the limit of these neighbourhoods is
$\operatorname{Spec}\kappa(\xi)$. It has $P$ by the second property
(compare [Stacks, [0F06](https://stacks.math.columbia.edu/tag/0F06)]), and so $\kappa(\xi)$ is the field asserted in the
lemma.
