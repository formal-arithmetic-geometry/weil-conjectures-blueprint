+++
kind  = "proof"
of    = "sk-i-real-boundary"
+++
*Step 0 (normality).* A smooth curve $C_0$ is normal, hence a finite
disjoint union of open and closed normal integral curves, and every
assertion below may be checked on each of them separately; a dense open
$U_0$ meets each of them. A *quasi-compact* etale scheme $W$ over a normal
Noetherian scheme is a finite disjoint union of open-and-closed
normal integral schemes: $W$ is Noetherian, its local rings are normal
domains because normality ascends along etale ring maps
([Stacks `033C`](https://stacks.math.columbia.edu/tag/033C)),
so its finitely many irreducible components are pairwise disjoint (a point
on two of them would give two minimal primes of its local domain) and
hence open and closed. Quasi-compactness cannot be dropped:
$\coprod_{m\in\mathbf N}\operatorname{Spec}k\to\operatorname{Spec}k$ is
etale but not a finite disjoint union. Every etale scheme to which this is
applied below is quasi-compact: the finite etale covers of Steps 3 and 4
and the affine etale $W\to Y$ of Step 3.

*Step 1 (constructibility at finite level, for any curve).* Here $C_0$ is
only assumed separated of finite type over $\Fq$ of dimension at most one,
$S_0=C_0\setminus U_0$ is finite, $\Lambda$ is a finite ring and
$\mathcal F$ is a finite locally constant sheaf of $\Lambda$-modules on
$U_0$. Since $C_0$ is a Jacobson space and $U_0$ is open with finite
complement, every point of $S_0$ is closed, so $C_0$ is stratified by $U_0$
and the finitely many locally closed points
$\operatorname{Spec}k(s)$, $s\in S_0$. On $U_0$ the restriction of
$j_*\mathcal F$ is $\mathcal F$, which is finite locally constant. A sheaf on
$\operatorname{Spec}k(s)$ is the discrete continuous
$\Gal(\overline{k(s)}/k(s))$-set given by its geometric stalk, and it is
finite locally constant as soon as that stalk is finite (the stabilizers are
open). So it remains to show that $(j_*\mathcal F)_{\bar s}$ is finite for
$s\in S_0$. Let $A=\mathcal O^{\mathrm{sh}}_{C_0,\bar s}$ be the strict
henselization, a Noetherian local ring of dimension at most one. As
$\mathcal F$ is represented by a finite etale $U_0$-scheme, a limit
argument gives
$(j_*\mathcal F)_{\bar s}=\Gamma(\operatorname{Spec}A\times_{C_0}U_0,\mathcal F)$.
The points of $\operatorname{Spec}A$ map to generizations of $s$, and no
point of $S_0$ other than $s$ is a generization of $s$, these points being
closed; hence $\operatorname{Spec}A\times_{C_0}U_0$ is the punctured
spectrum of $A$. As $\dim A\le1$, the punctured spectrum consists of the
finitely many minimal primes $\mathfrak p_1,\dots,\mathfrak p_m$ of $A$; they
are pairwise incomparable, so it is the finite disjoint union of the
$\operatorname{Spec}A_{\mathfrak p_i}$, each the spectrum of an Artinian
local ring (it is empty when $\dim A=0$). The etale site does not see
nilpotents, so
$$
(j_*\mathcal F)_{\bar s}=\prod_{i=1}^m\Gamma(\operatorname{Spec}\kappa(\mathfrak p_i),\mathcal F)
\subseteq\prod_{i=1}^m\mathcal F_{\bar\eta_i},
$$
for geometric points $\bar\eta_i$ over $\kappa(\mathfrak p_i)$, and each
$\mathcal F_{\bar\eta_i}$ is finite. Hence $(j_*\mathcal F)_{\bar s}$ is finite
and $j_*\mathcal F$ is constructible.

For the lisse Weil sheaf $\mathcal F$ of the statement, apply this to the
finite levels $\mathcal F_n$ of an $\mathcal O_E$-model, which are
locally constant sheaves of finite $\mathcal O_E/\mathfrak m_E^n$-modules;
so $j_*\mathcal F_n$ is constructible for every $n$. (A lisse
$\Qlb$-sheaf need not be trivialized by any finite etale cover: on
$\mathbf G_m$ the unipotent Kummer extension, on which $\mathbf Z_\ell(1)$
acts by $\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)$, has
infinite geometric monodromy; this is why one works at finite levels.) For
$J$ itself: $J|_{U_0}=\mathcal F$ is lisse, and at each of the finitely many
boundary points $s$ the stalk $J_{\bar s}=V_s^{I_s}$ of Step 2 is a
finite-dimensional representation of the residue Weil group, so $J$ is
lisse on each stratum of $U_0\sqcup(C_0\setminus U_0)$, i.e. constructible
in the sense of [sk-d-real-weil].

*Step 2 (the boundary stalk).* The stalk of $J$ at a geometric
boundary point $\bar s$ is computed on the punctured strict henselian
trait at $s$. The strict-henselization stalk formula is a statement
about torsion sheaves, so it is applied at each finite level: it
identifies $(j_*\mathcal F_n)_{\bar s}$ with the invariants $M_n^{I_s}$ of
the finite-level geometric generic stalk under the inertia group
$I_s=\Gal(\overline{K_s}/K_s^{\mathrm{sh}})$. The geometric stalk of the
adic sheaf $J$ is formed from these levels,
$J_{\bar s}=(\varprojlim_nM_n^{I_s})\otimes_{\mathcal O_E}E$; invariants
commute with inverse limits, so $\varprojlim_nM_n^{I_s}=M^{I_s}$ for the
lattice $M=\varprojlim_nM_n$ of $V_s$, and $M^{I_s}=M\cap V_s^{I_s}$ is
saturated in $M$, so $M^{I_s}\otimes_{\mathcal O_E}E=V_s^{I_s}$. (The
tower $(M_n^{I_s})_n$ need not be adic; only its limit enters.) Hence
$J_{\bar s}=V_s^{I_s}$,
where $K_s$ is the fraction field of the henselization as in
[sk-d-real-boundary] and $K_s^{\mathrm{sh}}\subset\overline{K_s}$ is
the fraction field of the strict henselization, the generic point of the
trait. Since $\Gal(K_s^{\mathrm{sh}}/K_s)=\Gal(\overline{k(s)}/k(s))$,
this is the kernel of
$\Gal(\overline{K_s}/K_s)\to\Gal(\overline{k(s)}/k(s))$ of
[sk-d-real-boundary], whereas $\Gal(\overline{K_s}/K_s)$ itself is the
decomposition group.
The Weil structures descend through the trait, so the identification is
equivariant for the residue Frobenius lift.

*Step 3 (lisse sheaves extend from a dense open).* For a finite
module $M$ on a normal integral Noetherian $Y$ and a nonempty open
$v:V\hookrightarrow Y$, the canonical map
$\underline M_Y\to v_*\underline M_V$ is an isomorphism: evaluate on an
affine etale $W\to Y$, decompose $W$ by Step 0, and note that each
component meets $W\times_YV$ because it is integral and $V$ is dense, so
a section over $W\times_YV$ is determined by, and extends to, a section
over $W$. For a finite locally constant sheaf $\mathcal G$ of $\Lambda$-modules on
the smooth curve $C_0$ and a dense open $U_0$, trivialize $\mathcal G$ by a
finite etale surjection $P\to C_0$; by Step 0 the scheme $P$ is a finite
disjoint union of normal integral curves $P_a$, each meeting the dense
inverse image of $U_0$, and $\mathcal G|_{P_a}$ is constant. The unit
$\mathcal G\to j_*j^*\mathcal G$ is compatible with pullback along the etale
map $P\to C_0$ (direct image along an open immersion commutes with etale
base change), and its pullback to each $P_a$ is the isomorphism just proved
for the constant sheaf; since $P\to C_0$ is surjective, the unit is an
isomorphism. For $\mathcal G$ lisse on $C_0$, apply this to each finite
level $\mathcal G_n$ to get
$\mathcal G_n\simeq j_*(\mathcal G_n|_{U_0})$ for every $n$; these
isomorphisms are compatible in $n$ and $j_*$ of an adic sheaf is formed
levelwise, so $\mathcal G\simeq j_*(\mathcal G|_{U_0})$. (Equivalently,
Step 2 at $s\in C_0\setminus U_0$ gives
$J_{\bar s}=\mathcal G_{\bar s}^{I_s}=\mathcal G_{\bar s}$, inertia acting
trivially on the stalk of a sheaf lisse at $s$.)

*Step 4 (surjectivity on fundamental groups).* Let $W\to C$ be
connected finite etale. By Step 0 it is normal integral, hence its
restriction $W\times_CU$ is again integral, so connected: a connected
cover of $C$ stays connected over the nonempty open $U$. Equivalently
$\pi_1(U)\to\pi_1(C)$ is surjective. The Weil-group map of
[sk-d-real-weil] is the pullback of this one along the degree map to
$\mathbf Z$, so it is surjective too.
