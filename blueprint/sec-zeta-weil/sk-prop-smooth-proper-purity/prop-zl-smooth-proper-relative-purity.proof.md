+++
kind  = "proof"
of    = "prop-zl-smooth-proper-relative-purity"
uses = ["cor-zl-rfshriek-sheaf", "cor-cbc-proper-coincidence", "prop-weil-operations", "sk-thm-sfb-qlbar-two-colimit", "thm-lisse-qlbar-representations", "sk-lem-stratified-lattice", "thm-fin-proper-constructibility-complete", "prop-weil-proet-finite-proper-base-change", "cor-weil-pbc-geometric-fiber-finite", "sbc-thm-smooth-base-change", "sk-thm-sfb-proper-base-change", "sk-prop-scalar-six", "sk-prop-pe-milnor", "sk-prop-sfb-finite-extension-compatibility", "cor-weil-pbc-geometric-fiber-qbar", "def-weil-punctual-weights", "lem-sf-hom-finite-projective", "lem-wf-tate-twist-frobenius", "lem-sf-tensor-hom", "sk-thm-purity-transport", "lem-sf-twist-interchange"]
+++
Write $f:X\to Y$ for the geometric fiber of $f_0$ and $\mathcal F$ for the
underlying sheaf of $\mathcal F_0$. The upper bound on weights is the
direct-image theorem [cor-zl-rfshriek-sheaf]; the content here is that
relative duality supplies the matching lower bound.

*Step 1 (coincidence and local constancy).* Since $f$ is proper, the
compactification $j=\operatorname{id}$, $p=f$ gives the canonical
identification $Rf_!\xrightarrow{\sim}Rf_*$ of
[cor-cbc-proper-coincidence], and under it the exchange map
$\operatorname{Ex}_!$ defining the Weil structure on $Rf_!\mathcal F$ is the
exchange map $\operatorname{Ex}_*$ defining the Weil structure on
$Rf_*\mathcal F$ ([cor-cbc-proper-coincidence], and the description of the
Weil isomorphisms in [prop-weil-operations]). Hence
$R^{i}f_{0!}\mathcal F_0\to R^{i}f_{0*}\mathcal F_0$ is an isomorphism of
Weil sheaves for every $i$; this is the first half of (a).

For local constancy we may treat each connected component of $X$ separately.
By [sk-thm-sfb-qlbar-two-colimit] (1),
$\mathcal F\cong\QbarX\otimes_{E_X}\mathcal F_E$ for a lisse $E_X$-module
$\mathcal F_E$ and a finite extension $E/\Ql$. Since $Y_0$ is normal and $f$
is smooth, $X$ is normal; by [thm-lisse-qlbar-representations],
$\mathcal F_E$ corresponds to a continuous representation of the profinite
group $\pi_1(X,\bar x)$ on a finite-dimensional $E$-vector space, which
stabilizes an $\mathcal O_E$-lattice by compactness, and the lattice gives a
lisse $\mathcal O_{E,X}$-submodule $L_0\subset\mathcal F_E$ with
$L_0[1/\ell]=\mathcal F_E$ (compare [sk-lem-stratified-lattice], where the
normality hypothesis is shown to be needed). Put
$\mathcal F_n=L_0\otimes_{\mathcal O_E}\mathcal O_E/\lambda^{n}$; each
$\mathcal F_n$ is a finite locally constant sheaf of
$\mathcal O_E/\lambda^{n}$-modules, of $\ell$-power torsion with $\ell$
invertible on $Y$, and may be treated on the étale site.
By [thm-fin-proper-constructibility-complete] the sheaves
$R^{q}f_*\mathcal F_n$ are constructible, and a constructible sheaf all of
whose specialization maps are isomorphisms is locally constant; so it
suffices to show that for a geometric point $\bar s$ of $Y$ and a geometric
point $\bar t$ of the strict henselization $Y'=Y_{(\bar s)}$ the
specialization map
$(R^{q}f_*\mathcal F_n)_{\bar s}\to(R^{q}f_*\mathcal F_n)_{\bar t}$ is an
isomorphism. Proper base change
[prop-weil-proet-finite-proper-base-change] along $Y'\to Y$ lets us replace
$f$ by its base change $f':X'\to Y'$, which is again smooth and proper, with
closed point $\bar s$; then
$(R^{q}f'_*\mathcal F_n)_{\bar s}=H^{q}(X',\mathcal F_n)$ ($Y'$ being strictly
local), the geometric-fibre formula [cor-weil-pbc-geometric-fiber-finite]
identifies $(R^{q}f'_*\mathcal F_n)_{\bar t}$ with
$H^{q}(X'_{\bar t},\mathcal F_n)$, and the specialization map becomes the
restriction along $h:X'_{\bar t}\to X'$. We show that
$\mathcal F_n\to Rh_*h^{-1}\mathcal F_n$ restricts to an isomorphism on the
closed fibre $X'_{\bar s}$. The question is étale local on $X'$ and
$R^{q}h_*$ commutes with étale restriction, so we may pass to an étale
$U\to X'$ on which $\mathcal F_n$ is constant, with value $M$; the composite
$U\to Y'$ is smooth, and smooth base change [sbc-thm-smooth-base-change],
applied to the cartesian square formed by $U\to Y'$ and the
quasi-compact quasi-separated $\bar t:\Spec\Omega\to Y'$ and to the
constant sheaf $M$ on $\Spec\Omega$, gives
$R^{q}h_{U*}M\cong(U\to Y')^{-1}R^{q}\bar t_*M$. As $Y'$ is strictly local,
the stalk of $R^{q}\bar t_*M$ at $\bar s$ is $H^{q}(\Spec\Omega,M)$, which is
$M$ for $q=0$ and $0$ for $q>0$ since $\Omega$ is separably closed. Thus
$(Rh_*h^{-1}\mathcal F_n)|_{X'_{\bar s}}\cong\mathcal F_n|_{X'_{\bar s}}$.
Applying [cor-weil-pbc-geometric-fiber-finite] at the closed point
$\bar s$ of the strictly local $Y'$ twice, to
$K=Rh_*h^{-1}\mathcal F_n\in D^+(X',\mathcal O_E/\lambda^{n})$ and to
$\mathcal F_n$, we get

$$
H^{q}(X'_{\bar t},\mathcal F_n)=H^{q}(X',Rh_*h^{-1}\mathcal F_n)
\cong H^{q}\bigl(X'_{\bar s},(Rh_*h^{-1}\mathcal F_n)|_{X'_{\bar s}}\bigr)
\cong H^{q}(X'_{\bar s},\mathcal F_n)\cong H^{q}(X',\mathcal F_n),
$$

compatibly with restriction along $h$. So every specialization map is an
isomorphism, and every $R^{q}f_*\mathcal F_n$ is finite locally constant.
No separate local-acyclicity theorem is needed: the vanishing of
$R^{q}h_*$ along the closed fibre is exactly what smooth base change
supplies. The $\ell$-adic statement is a consequence of the condensed comparison
theorems. By [sk-thm-sfb-proper-base-change],
$Rf_*L_0\in\Dbc(Y,\mathcal O_E)$, and the coefficient comparison for $Rf_*$
along $\mathcal O_E\to\mathcal O_E/\lambda^n$ ([sk-prop-scalar-six]) gives
$Rf_*L_0\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\lambda^n\simeq Rf_*\mathcal F_n$.
As $Rf_*L_0$ is derived $\lambda$-complete, it is the derived limit of these
reductions, and the Milnor sequence ([sk-prop-pe-milnor]), whose
$\varprojlim^1$-terms vanish because the transition maps between the finite
locally constant sheaves $R^{i-1}f_*\mathcal F_n$ satisfy the Mittag-Leffler
condition locally, gives
$R^{i}f_*L_0\cong\varprojlim_nR^{i}f_*\mathcal F_n$. On each connected
component of $Y$ this is the limit of a compatible system of finite
continuous $\pi_1(Y,\bar y)$-modules, i.e. a lisse
$\mathcal O_{E,Y}$-module, possibly with torsion. Extension of scalars along
the flat maps $\mathcal O_E\to E\to\Qlb$ is exact and commutes with $Rf_*$
([sk-prop-scalar-six], [sk-prop-sfb-finite-extension-compatibility]), so
$R^{i}f_*\mathcal F\cong\Qlb\otimes_{\mathcal O_E}R^{i}f_*L_0$ is a lisse
$\QbarY$-module; its stalks are computed by
[cor-weil-pbc-geometric-fiber-qbar]. This completes (a).

*Step 2 (upper bound).* A punctually $\iota$-pure sheaf of weight $w$ is
$\iota$-mixed of weights at most $w$ in the sense of
[def-weil-punctual-weights] (take $m=1$, $w_1=w$). Hence
[cor-zl-rfshriek-sheaf], applied to the separated finite-type
$f_0$, shows that $R^{i}f_{0!}\mathcal F_0=R^{i}f_{0*}\mathcal F_0$ is
$\iota$-mixed of weights at most $w+i$. Taking the stalk at $\bar y$ of the
filtration in [def-weil-punctual-weights] is exact and $F_y$-equivariant,
so every eigenvalue $\alpha$ of $F_y$ on $(R^{i}f_{0*}\mathcal F_0)_{\bar y}$
is an eigenvalue on a graded piece of some weight $w_r\leq w+i$, whence
$|\iota(\alpha)|\leq q_y^{(w+i)/2}$.

*Step 3 (lower bound by relative Verdier duality).* Let
$\mathcal F_0^\vee=R\mathcal H om(\mathcal F_0,\Qlb)$ be the coefficient dual
of $\mathcal F_0$: since $\mathcal F$ is lisse, it is locally on the site a
finite free $\Qlb$-module, so by [lem-sf-hom-finite-projective]
$\mathcal F^\vee$ is concentrated in degree $0$, lisse, and a Weil sheaf by
[prop-weil-operations]; its local Frobenius at a closed point $x$ is the
contragredient of that of $\mathcal F_0$, so its eigenvalues are the
$\beta^{-1}$ with $\beta$ an eigenvalue of $F_x$ on $\mathcal F_{\bar x}$,
and as $|\iota(\beta^{-1})|=|\iota(\beta)|^{-1}=q_x^{-w/2}$ it is
punctually $\iota$-pure of weight $-w$. By
[lem-wf-tate-twist-frobenius] the local Frobenius on $\Qlb(d)_{\bar x}$
is $q_x^{-d}$, so $\mathcal F_0^\vee(d)$ is lisse and punctually
$\iota$-pure of weight $-w-2d$.

The relative duality isomorphism is assembled from three canonical
isomorphisms, each a morphism of Weil complexes by [prop-weil-operations]
(composition, purity and duality isomorphisms are Weil). First, the
tensor–Hom form of the Verdier exchange [lem-sf-tensor-hom], applied to
$f$ with $M=\mathcal F$ and $N=\Qlb_Y$, together with $Rf_!=Rf_*$
from Step 1:

$$
Rf_*R\mathcal H om_X\bigl(\mathcal F,Rf^!\Qlb_Y\bigr)\xrightarrow{\ \sim\ }
R\mathcal H om_Y\bigl(Rf_*\mathcal F,\Qlb_Y\bigr).
$$

Second, the smooth orientation: [sk-thm-purity-transport], for the
smooth separated $f$ of relative dimension $d$, $\Lambda=\Qlb$ and
$K=\Qlb_Y$, gives $\Qlb_X(d)[2d]=Lf^*\Qlb_Y(d)[2d]\xrightarrow{\sim}Rf^!\Qlb_Y$.
Third, the perfect form of duality: $\mathcal F$ is perfect over
$\Qlb_X$, so [lem-sf-twist-interchange] with $m=d$, $n=2d$ gives
$R\mathcal H om_X(\mathcal F,\Qlb_X(d)[2d])\cong\mathcal F^\vee(d)[2d]$.
Composing,

$$
R\mathcal H om_Y\bigl(Rf_*\mathcal F,\Qlb_Y\bigr)\;\cong\;
Rf_*\bigl(\mathcal F^\vee(d)\bigr)[2d]
$$

as Weil complexes on $Y$. By Step 1 the cohomology sheaves
$R^{j}f_*\mathcal F$ of $Rf_*\mathcal F$ are lisse; for a lisse sheaf
$\mathcal L$ on $Y$, [lem-sf-hom-finite-projective] (locally on the site
$\mathcal L$ is finite free) gives
$\mathcal E xt^{r}(\mathcal L,\Qlb_Y)=0$ for $r>0$ and
$\mathcal H om(\mathcal L,\Qlb_Y)=\mathcal L^\vee$ lisse, with stalks the
linear duals of those of $\mathcal L$. Induction on the truncation
triangles of the bounded complex $Rf_*\mathcal F$ therefore identifies the
cohomology sheaf in degree $-i$ of the left side with
$(R^{i}f_*\mathcal F)^\vee$. Taking $\mathcal H^{-i}$ of both sides gives the
Frobenius-equivariant isomorphism of lisse sheaves

$$
\bigl(R^{i}f_{0*}\mathcal F_0\bigr)^{\vee}
\;\cong\;
R^{2d-i}f_{0*}\bigl(\mathcal F_0^{\vee}(d)\bigr).
$$

Now fix a closed point $y\in|Y_0|$ and $\bar y$ over it. Step 2 applied to
the lisse, punctually pure $\mathcal F_0^\vee(d)$ of weight $-w-2d$ in degree
$2d-i$ bounds every eigenvalue $\gamma$ of $F_y$ on the right-hand stalk by
$|\iota(\gamma)|\leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}$. The left-hand
sheaf being the dual of a lisse sheaf, its stalk at $\bar y$ is the
linear dual of $(R^{i}f_{0*}\mathcal F_0)_{\bar y}$ with the contragredient
action of $F_y$, whose eigenvalues are the $\alpha^{-1}$ with $\alpha$ an
eigenvalue of $F_y$ on $(R^{i}f_{0*}\mathcal F_0)_{\bar y}$. Hence
$|\iota(\alpha)|^{-1}\leq q_y^{(-w-i)/2}$, i.e.

$$
|\iota(\alpha)|\geq q_y^{(w+i)/2}.
$$

With Step 2 this gives $|\iota(\alpha)|=q_y^{(w+i)/2}$ for every
eigenvalue of every $F_y$, which is punctual $\iota$-purity of weight $w+i$.
This proves (b).

*What the upgrade costs.* Steps 1 and 3 use only smoothness, properness and
duality; no no-cancellation argument enters, because purity is read off
eigenvalue by eigenvalue. All the arithmetic sits in
[cor-zl-rfshriek-sheaf]: without it Step 3 bounds nothing, and with it both
inequalities are automatic.
