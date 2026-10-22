+++
kind  = "proof"
of    = "thm-pc-semicontinuity-base-change"
+++
*Local model.* Fix $t\in T$. By [lem-pc-rf-perfect-base-change](1),
applied over an affine open neighbourhood of $t$, there are an open
$V\ni t$ and a bounded complex $P$ of finite free $\mathcal O_V$-modules
such that $\mathcal H^q(g^*P)\cong R^qf'_*\mathcal F'$ for every
$g:T'\to V$ (notation as there). Shrinking $V$ to an affine open
$U=\operatorname{Spec}(A)\ni t$, we may assume

$$
P|_U\cong\widetilde K,\qquad
K:\;0\to K^a\xrightarrow{d^a}K^{a+1}\to\cdots\to K^b\to0,\qquad
K^i\cong A^{n_i}.
$$

Taking for $g$ the inclusion of $U$ gives
$R^qf_*\mathcal F|_U\cong\widetilde{H^q(K)}$. For $s\in U$ let
$g_s:\operatorname{Spec}\kappa(s)\to U$ be the canonical morphism and
$f_s:X_s\to\operatorname{Spec}\kappa(s)$ the fibre. Then $g_s^*P$ is the
complex $K\otimes_A\kappa(s)$ of finite dimensional vector spaces, and
the target is a one-point space, on which the $q$-th higher direct
image is the $q$-th cohomology group; hence

$$
H^q(X_s,\mathcal F_s)\cong H^q(K\otimes_A\kappa(s)),
$$

a finite dimensional $\kappa(s)$-vector space.

*(1).* Finite dimensionality was just shown. The map $\varphi^q(t)$ is
the canonical base-change map $g_t^*R^qf_*\mathcal F\to
R^qf_{t,*}\mathcal F_t$ attached to the cartesian square with bottom arrow
$g_t$; over an affine neighbourhood $\operatorname{Spec}(A)$ of $t$ it is
the map
$\kappa(t)\otimes_AH^q(\check C^\bullet)\to H^q(\check C^\bullet\otimes_A\kappa(t))$,
$1\otimes[z]\mapsto[z\otimes1]$, for the Cech complex $\check C^\bullet$ of
a finite affine cover of $X_{\operatorname{Spec}(A)}$, using
$\check C^\bullet\otimes_A\kappa(t)=\check C^\bullet(\mathcal U_t,\mathcal F_t)$
([lem-pc-rf-base-change-flat-module]) and [lem-pc-cech-resolution] on
both sides. It is well defined because a cycle (resp. boundary) maps to
a cycle (resp. boundary).

*(2).* Write $d^i(s)=d^i\otimes_A\kappa(s)$ for the matrix of $d^i$
with entries reduced to $\kappa(s)$, and let
$\rho_i(s)=\operatorname{rank}d^i(s)$. Linear algebra over $\kappa(s)$
gives

$$
\beta^q(s)=n_q-\rho_q(s)-\rho_{q-1}(s)\qquad(s\in U).
$$

For every integer $r$, the set $\{s:\rho_i(s)\ge r\}$ is the set of
points at which some $r\times r$ minor of $d^i$ does not vanish, i.e.
the complement of the closed set $V(I_r(d^i))$ cut out by the ideal of
$r\times r$ minors. Hence each $\rho_i$ is lower semicontinuous on
$U$, so $\beta^q$ is upper semicontinuous on $U$. Such opens $U$ cover
$T$, and upper semicontinuity is local, which proves (2).

*(3).* Now let $T$ be reduced, hence $A$ reduced, and let $\beta^q$ be
locally constant. Shrinking $U$ around $t$ we may assume $\beta^q$ is
constant on $U$, so $\rho_q+\rho_{q-1}=c$ is constant. Then
$\rho_q=c-\rho_{q-1}$ is also upper semicontinuous, hence locally
constant, and likewise $\rho_{q-1}$. Shrinking $U$ once more, we may
assume $\rho_q\equiv r$ and $\rho_{q-1}\equiv r'$ on $U$.

*Claim.* Let $\phi:A^m\to A^n$ be a matrix over a reduced ring $A$
whose rank at every point of $\operatorname{Spec}(A)$ equals $r$. Then
every point has a principal open neighbourhood over which, in suitable
bases, $\phi=\begin{pmatrix}I_r&0\\0&0\end{pmatrix}$. Indeed, every
$(r+1)\times(r+1)$ minor of $\phi$ vanishes in every residue field,
hence lies in every prime ideal, hence is nilpotent, hence is $0$ since
$A$ is reduced. At a given point some $r\times r$ minor $\delta$ is
nonzero, so $\delta$ is a unit on $D(\delta)$. After permuting bases,
$\phi=\begin{pmatrix}D&B\\C&F\end{pmatrix}$ with $D$ invertible over
$A_\delta$; invertible row and column operations bring $\phi$ to
$\begin{pmatrix}I_r&0\\0&F'\end{pmatrix}$ with $F'=F-CD^{-1}B$. The
$(r+1)\times(r+1)$ minors of the new matrix are
$A_\delta$-linear combinations of those of $\phi$ (Cauchy–Binet), so
they vanish; the minor formed by $I_r$ and one entry of $F'$ equals
that entry, so $F'=0$.

Apply the claim to $d^q$ and to $d^{q-1}$ and shrink $U$ to a principal
open neighbourhood of $t$ on which both normal forms hold (the bases
used for the two maps need not agree). Then
$Z=\ker d^q$ is a direct summand of $K^q$, free of rank $n_q-r$, with a
complement $Z'$ mapped by $d^q$ isomorphically onto a direct summand of
$K^{q+1}$; and $B=\operatorname{im}d^{q-1}$ is a direct summand of
$K^q$, free of rank $r'$, with $K^{q-1}\to B$ a split surjection.
Since $B\subseteq Z$, a retraction $K^q\to B$ restricts to a retraction
$Z\to B$, so $B$ is a direct summand of $Z$ and

$$
H^q(K)=Z/B
$$

is a finite projective $A$-module of rank $n_q-r-r'=\beta^q(t)$. Being
finite projective, it is locally free on principal opens, so
$R^qf_*\mathcal F$ is finite locally free near $t$, in particular flat.

Since $t$ was arbitrary, (3) follows.

*(4).* Let $T$ be reduced and locally Noetherian and let $\beta^q$ be
constant on the generizations of $t$. Choose an affine Noetherian open
$\operatorname{Spec}(A)\ni t$ and a finite affine cover $\mathcal U$ of its
inverse image in $X$. By [lem-pc-rf-perfect-base-change](2),(3) the Cech
complex $\check C^\bullet$ is perfect in $D(A)$ and its formation
commutes with base change to every affine $\operatorname{Spec}(B)$. As in
the local model, after replacing $A$ by a principal localization
(which localizes $\check C^\bullet$), $\check C^\bullet$ is isomorphic in
$D(A)$ to a bounded complex $K$ of finite free $A$-modules. Both are
complexes of flat modules up to the bounded flat truncation of
[lem-pc-rf-base-change-flat-module], so the isomorphism survives
$\otimes_A\kappa(s)$ for all $s$ ([lem-pc-flat-complex-derived-pullback]),
and $\varphi^q(t)$ becomes the evident map
$H^q(K)\otimes_A\kappa(t)\to H^q(K\otimes_A\kappa(t))$, while
$\beta^q(s)=\dim H^q(K\otimes_A\kappa(s))$.

Let $\mathfrak p$ be the prime of $t$ and pass to $A_{\mathfrak p}$, which is
reduced; its points are exactly the generizations of $t$, so $\beta^q$ is
constant on $\operatorname{Spec}A_{\mathfrak p}$, and
$H^q(K)\otimes_A\kappa(t)=H^q(K_{\mathfrak p})\otimes_{A_{\mathfrak p}}\kappa(t)$.
With $\rho_i$ as in (2), $\rho_q+\rho_{q-1}$ is constant on
$\operatorname{Spec}A_{\mathfrak p}$. Each $\rho_i$ is lower semicontinuous,
so $\{\rho_i\ge\rho_i(t)\}$ is an open set containing the closed point $t$
of the local scheme, hence everything; as the sum is constant, both
$\rho_q$ and $\rho_{q-1}$ are constant. The *Claim* of (3) over the reduced
local ring $A_{\mathfrak p}$ (whose only principal open containing the
closed point is the whole spectrum) puts $d^q$ and $d^{q-1}$ in normal
form, and as in (3) we get $Z=\ker d^q$ and $B=\operatorname{im}d^{q-1}$
as direct summands of $K^q_{\mathfrak p}$ with $B$ a direct summand of $Z$.
Split injections and split surjections remain so after
$\otimes\kappa(t)$. Thus $d^q(t)$ is injective on a complement of
$Z\otimes\kappa(t)$ and zero on $Z\otimes\kappa(t)$, giving
$\ker d^q(t)=Z\otimes\kappa(t)$; and
$\operatorname{im}d^{q-1}(t)=B\otimes\kappa(t)$. The split exact sequence
$0\to B\to Z\to Z/B\to0$ stays exact after tensoring, so

$$
H^q(K\otimes_A\kappa(t))
=\frac{Z\otimes\kappa(t)}{B\otimes\kappa(t)}
=H^q(K_{\mathfrak p})\otimes\kappa(t),
$$

and the identification is exactly the map $\varphi^q(t)$. This proves (4).

*Why reducedness is needed.* Let $A=k[\varepsilon]/(\varepsilon^2)$ and let
$E_0$ be an elliptic curve over the field $k$. Let $\mathcal L$ be an invertible
sheaf on $E_0\times_k\operatorname{Spec}A$ that restricts to
$\mathcal O_{E_0}$ but is a nontrivial first-order deformation of it
(these are classified by the nonzero elements of
$H^1(E_0,\mathcal O_{E_0})\cong k$). A global section of $\mathcal L$
reduces to a constant on $E_0$. A nonzero constant cannot lift, since
a lift would trivialise $\mathcal L$. Hence
$H^0(\mathcal L)=\varepsilon H^0(E_0,\mathcal O_{E_0})\cong k$, a
module killed by $\varepsilon$ and so not flat over $A$. The base is a
single point, so $\beta^0$ is constant.
