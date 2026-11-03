+++
kind  = "proof"
of    = "sk-prop-normal-form"
+++
*Normal form.* Shrinking to affines, write $X=\Spec B$,
$Y=\Spec A$ with $B=A[t_1,\dots,t_n]/(g_1,\dots,g_c)$ and the
Jacobian $(\partial g_i/\partial t_j)$ of rank $c=n-d$ at $x$. Pick
$d$ of the coordinates whose differentials complete the $c$ rows of
the Jacobian to a basis of
$\Omega_{A[t]/A}\otimes\kappa(x)$; they define a $Y$-morphism
$e:X\to\Aaf^d_Y$ with $\Omega_{X/\Aaf^d_Y}=0$ near $x$, i.e. $e$
unramified. Source and target are smooth over $Y$ of the same
relative dimension $d$, but $Y$ is arbitrary, so miracle flatness
cannot be applied to $e$ itself; apply it fibrewise. For $y\in Y$
the fibre $e_y:X_y\to\Aaf^d_{\kappa(y)}$ is an unramified morphism of
smooth $\kappa(y)$-schemes of dimension $d$; its fibres are
$0$-dimensional, and the local rings at $x$ and $e(x)$ are regular of
the same dimension (unramified morphisms have finite residue
extensions, so $x$ and $e(x)$ have the same transcendence degree over
$\kappa(y)$), so miracle flatness (regular target, Cohen–Macaulay
source, $\dim$ source $=\dim$ target $+$ fibre dimension) makes $e_y$
flat at $x$. Since $X$ and $\Aaf^d_Y$ are flat and locally of finite
presentation over $Y$, the fibrewise flatness criterion makes $e$
flat at $x$, and flat $+$ unramified $=$ étale. (Equivalently: a
$Y$-morphism of $Y$-smooth schemes is étale at $x$ as soon as it
induces an isomorphism on $\Omega_{-/Y}\otimes\kappa(x)$, which the
choice of coordinates guarantees.) Composing with $p_d$ returns $g$
by construction.

*Slicing and relative connectedness, $f$ smooth.* We may assume $X$
and $S$ affine. Let $x\in X$ be a point
*closed in its own fibre* $X_s$, $s=f(x)$, *with
$\kappa(x)/\kappa(s)$ separable*. Then
$\mathfrak m_x/\mathfrak m_x^2$ computed in the smooth
$\kappa(s)$-scheme $X_s$ has dimension $d=\dim_xX_s$ and maps
isomorphically onto
$\Omega_{X_s/\kappa(s)}\otimes\kappa(x)=\Omega_{X/S}\otimes\kappa(x)$
(the cokernel of this map is $\Omega_{\kappa(x)/\kappa(s)}$, which
vanishes exactly because the finite extension is separable; without
separability no such sections exist, e.g. $S=\Spec\mathbf F_p(t)$,
$X=\Aaf^1_S$, $x$ given by $u^p=t$), so one may cut
$X$ near $x$ by $d$ sections of $\mathcal O_X$ vanishing at $x$ whose
differentials are a basis of $\Omega_{X/S}\otimes\kappa(x)$; the
resulting closed subscheme
$V\subseteq X$ is smooth of relative dimension $0$ over $S$ at $x$ by
the Jacobian
criterion, i.e. étale there, so after shrinking $V\to S$ is
étale and $(\iota,\mathrm{id}):V\to X\times_SV$ is a section of the
smooth $X\times_SV\to V$. Let $U\subseteq X\times_SV$ be the
relative connected component of that section, i.e. the set of points
lying in the same connected component of their own fibre as the
section; it is open by the open representability of the relative
connected-component functor for a flat, finitely presented morphism
with geometrically unibranch (here: smooth) fibres. Then $U\to V$
is smooth with geometrically connected fibres and a section, $V\to S$
is étale, and $U\to X\times_SV\to X$ is étale. These $U$ cover
$X$: the image $W_x$ of $U\to X$ is open and contains the whole
connected component of $x$ in $X_s$, because the fibre of $U$ over
the point $x\in V$ is the connected component of
$X_s\otimes_{\kappa(s)}\kappa(x)$ through the section point, and the
finite étale surjection $X_s\otimes_{\kappa(s)}\kappa(x)\to X_s$
($\kappa(x)/\kappa(s)$ finite separable) maps connected components
onto connected components. Connected components of the locally
noetherian $X_s$ are open, and every nonempty open of the smooth
$\kappa(s)$-scheme $X_s$ contains a point closed in $X_s$ with
separable residue field (by the normal form it contains an open
étale over $\Aaf^d_{\kappa(s)}$, whose points with coordinates in a
separable closure are dense, and étale maps have separable residue
extensions). Hence every connected component of every fibre lies in
some $W_x$, and $\bigcup_xW_x=X$.

*Making $U\to V$ affine, $f$ smooth.* Covering $V$ by affine opens, we
may assume $V$ affine; then $X\times_SV$ is affine. The geometric fibres
of $U\to V$ are smooth and connected, hence irreducible. Given a point
$z\in U$, lying over $v\in V$, prime avoidance gives a principal open
$D(a)\subseteq X\times_SV$ contained in the open $U$ and containing both $z$
and $\sigma(v)$. Choose an affine open $V'\ni v$ of $V$ with
$\sigma(V')\subseteq D(a)$ and put $U'=D(a)\times_VV'$, which is affine.
The fibres of $U'\to V'$ are nonempty open subsets of the geometrically
irreducible fibres of $U\to V$, so they are geometrically connected;
$\sigma$ restricts to a section, and $U'\to V'$ is smooth and affine. The
images of these $U'$ in $X$, over all $z\in U$, cover the image of $U$, so
they still cover $X$.

*The general case.* Now let $f$ be flat, locally of finite presentation,
with geometrically reduced fibres. The locus $X^{\mathrm{sm}}\subseteq X$
where $f$ is smooth is open, and $X^{\mathrm{sm}}\cap X_s$ is dense in every
fibre $X_s$, because a geometrically reduced scheme locally of finite type
over a field is smooth over it on a dense open. Run the slicing step at the
points $x\in X^{\mathrm{sm}}$ closed in $X_s$ with $\kappa(x)/\kappa(s)$
separable: it gives $V\to S$ étale and a section $\sigma$ of
$X\times_SV\to V$ through $X^{\mathrm{sm}}\times_SV$. Let
$U\subseteq X\times_SV$ be the relative connected component of $\sigma$;
for a flat morphism locally of finite presentation with geometrically
reduced fibres it is open, and $U\to V$ is flat, locally of finite
presentation, with geometrically connected fibres and the section
$\sigma$, while $U\to X$ is étale. As in the smooth case, the image of $U$
in $X$ contains the connected component of $x$ in $X_s$. Every connected
component of $X_s$ meets the dense subset $X^{\mathrm{sm}}\cap X_s$ and so
contains such a point $x$; hence these images cover $X$. To make $U\to V$
affine, the smooth-case argument does not apply, since the fibres of
$U\to V$ need not be irreducible and an affine open neighbourhood of the
section may disconnect them; this last step is Stacks, More on Morphisms,
Lemma 37.46.3 ([`0EY5`](https://stacks.math.columbia.edu/tag/0EY5)), and is
not proved here.
