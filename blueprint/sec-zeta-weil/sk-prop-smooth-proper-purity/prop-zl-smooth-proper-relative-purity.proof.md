+++
kind  = "proof"
of    = "prop-zl-smooth-proper-relative-purity"
uses = ["cor-zl-rfshriek-sheaf", "cor-cbc-proper-coincidence", "prop-weil-operations", "sk-lem-lisse-finite-descent", "thm-lisse-qlbar-representations", "sk-lem-stratified-lattice", "det-lem-stratified-lattice-scheme", "sk-prop-pbc-degree-zero", "cor-galois-lisse-representations", "thm-galois-fundamental", "sk-prop-pe-condensed-point", "sk-prop-sfb-qlbar-colimit-x", "sk-def-sfb-constructible", "thm-fin-proper-constructibility-complete", "prop-weil-proet-finite-proper-base-change", "cor-weil-pbc-geometric-fiber-finite", "sbc-thm-smooth-base-change", "sk-thm-sfb-proper-base-change", "sk-prop-scalar-six", "sk-prop-pe-milnor", "det-prop-sfb-finite-extension-compatibility", "cor-weil-pbc-geometric-fiber-qbar", "thm-weil-pbc-qbar", "def-weil-punctual-weights", "lem-sf-hom-finite-projective", "lem-wf-tate-twist-frobenius", "thm-pod-degreewise-perfectness-over-a-field", "thm-pod-equivariance-of-the-twisted-pairing"]
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

*Lattices étale-locally on $Y$.* Local constancy is local on $Y$. For an
étale $V\to Y$ the base change $f_V:X_V=X\times_YV\to V$ is again smooth and
proper, and proper base change ([sk-thm-sfb-proper-base-change]) identifies
$(R^{i}f_*\mathcal F)|_V$ with $R^{i}f_{V*}(\mathcal F|_{X_V})$, restriction
along $V\to Y$ being exact. By [sk-lem-lisse-finite-descent],
$\mathcal F\cong\QbarX\otimes_{E_X}\mathcal F_E$ for a lisse $E_X$-module
$\mathcal F_E$ and a finite extension $E/\Ql$. Treating the finitely many
connected components of $X$ separately, we may assume that $\mathcal F_E$ has
constant rank $r$. A *lattice* in $\mathcal F_E$ is a lisse
$\mathcal O_{E,X}$-submodule $L_0\subset\mathcal F_E$ with
$L_0[1/\ell]=\mathcal F_E$; it need not exist on all of $X$ when $X$ is not
normal ([sk-lem-stratified-lattice]). We show that every geometric point
$\bar y$ of $Y$ has an étale neighbourhood $V$ such that
$\mathcal F_E|_{X_V}$ has one. Let $q:\mathrm{Lat}\to X$ be the separated
étale $X$-scheme of lattices of $\mathcal F_E$
([det-lem-stratified-lattice-scheme]), and let $S$ be the étale sheaf of
sets on $X$ that it represents; for an étale $X$-scheme $T$, $S(T)$ is the
set of lattices in $\mathcal F_E|_T$. The geometric fibre $X_{\bar y}$ is
smooth over a separably closed field, hence a finite disjoint union of
connected normal Noetherian schemes, so $\mathcal F_E|_{X_{\bar y}}$ has a
lattice $M$ ([thm-lisse-qlbar-representations] (4)). On a pro-étale cover of
$X$ trivializing $\mathcal F_E$, both $\mathrm{Lat}$ and the sheaf of
lattices are constant with value the discrete set of $\mathcal O_E$-lattices
in $E^r$ ([det-lem-stratified-lattice-scheme] (1)), and the same holds after
base change of this cover to $X_{\bar y}$. So $M$ is, locally on
$X_{\bar y}$, a locally constant function to that set, and these local
sections glue to a section of $\mathrm{Lat}\times_XX_{\bar y}\to X_{\bar y}$,
that is, an element of $\Gamma(X_{\bar y},S|_{X_{\bar y}})$. Proper base
change in degree zero ([sk-prop-pbc-degree-zero]) gives
$(f_*S)_{\bar y}\cong\Gamma(X_{\bar y},S|_{X_{\bar y}})\neq\emptyset$, so
there is an étale neighbourhood $V$ of $\bar y$ with
$S(X_V)=(f_*S)(V)\neq\emptyset$: the sheaf $\mathcal F_E|_{X_V}$ has a
lattice. Replacing $f$ by $f_V$, we may therefore assume that $\mathcal F_E$
has a lattice $L_0$.

*Local constancy at finite level.* Put
$\mathcal F_n=L_0\otimes_{\mathcal O_E}\mathcal O_E/\pi_E^{n}$; each
$\mathcal F_n$ is a finite locally constant sheaf of
$\mathcal O_E/\pi_E^{n}$-modules, of $\ell$-power torsion with $\ell$
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
$K=Rh_*h^{-1}\mathcal F_n\in D^+(X',\mathcal O_E/\pi_E^{n})$ and to
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
supplies.

*Passage to the limit.* The $\ell$-adic statement is a consequence of the
condensed comparison theorems. By [sk-thm-sfb-proper-base-change],
$Rf_*L_0\in\Dbc(Y,\mathcal O_E)$, and the coefficient comparison for $Rf_*$
along $\mathcal O_E\to\mathcal O_E/\pi_E^n$ ([sk-prop-scalar-six]) gives
$Rf_*L_0\otimes^{\mathbf L}_{\mathcal O_E}\mathcal O_E/\pi_E^n\simeq Rf_*\mathcal F_n$.
As $Rf_*L_0$ is derived $\pi_E$-complete, it is the derived limit of these
reductions, and the Milnor sequence ([sk-prop-pe-milnor]), whose
$\varprojlim^1$-terms vanish because the transition maps between the finite
locally constant sheaves $R^{i-1}f_*\mathcal F_n$ satisfy the Mittag-Leffler
condition locally, gives
$R^{i}f_*L_0\cong\varprojlim_nR^{i}f_*\mathcal F_n$.

Fix a connected component of $Y$ and a geometric point $\bar y$ on it. By
[cor-galois-lisse-representations] the finite locally constant sheaves
$R^{i}f_*\mathcal F_n$ correspond to finite continuous
$\pi_1(Y,\bar y)$-modules $N_n=(R^{i}f_*\mathcal F_n)_{\bar y}$, compatibly
in $n$. As in the proof of essential surjectivity in
[thm-lisse-qlbar-representations] (1), let $Y_n\to Y$ be the connected finite
étale Galois cover belonging to the kernel of the action on
$N_1\oplus\dots\oplus N_n$ ([thm-galois-fundamental]) and
$\widetilde Y=\varprojlim_nY_n$; then $\widetilde Y\to Y$ is a pro-étale
cover on which every $R^{i}f_*\mathcal F_n$ is the constant sheaf
$(N_n)_{\widetilde Y}$, compatibly in $n$, so
$R^{i}f_*L_0|_{\widetilde Y}\cong\varprojlim_n(N_n)_{\widetilde Y}$. By
[cor-weil-pbc-geometric-fiber-finite], $N_n=H^{i}(X_{\bar y},\mathcal F_n)$,
so the Milnor sequence on $X_{\bar y}$, whose $\varprojlim^1$-term vanishes
because the groups $H^{i-1}(X_{\bar y},\mathcal F_n)$ are finite, gives
$N:=\varprojlim_nN_n\cong H^{i}(X_{\bar y},L_0)$. This is a finitely generated
$\mathcal O_E$-module: by [sk-thm-sfb-proper-base-change] for
$X_{\bar y}\to\Spec\kappa(\bar y)$, $R\Gamma(X_{\bar y},L_0)$ is bounded with
constructible cohomology on a point, where every pro-étale cover has a
section ([sk-prop-pe-condensed-point]), so its cohomology groups are finitely
presented. The system $(N_n)$ of finite modules is Mittag-Leffler, hence
pro-isomorphic to the system of its stable images, which are the images
$N/U_n$ of $N$; the $U_n$ are open submodules of the compact module $N$ with
$\bigcap_nU_n=0$, hence cofinal with the $\pi_E^nN$. Pro-isomorphic systems
have isomorphic limits, so, writing $N$ as a finite sum of copies of
$\mathcal O_E$ and of $\mathcal O_E/\pi_E^a$ and using
$\mathcal O_{E,\widetilde Y}\cong\varprojlim_n(\mathcal O_E/\pi_E^n)_{\widetilde Y}$
([sk-prop-sfb-qlbar-colimit-x]),

$$
R^{i}f_*L_0|_{\widetilde Y}\cong\varprojlim_n(N/\pi_E^nN)_{\widetilde Y}
\cong\mathcal O_{E,\widetilde Y}\otimes_{\mathcal O_E}N .
$$

So $R^{i}f_*L_0$ has a finite constant local model
([sk-def-sfb-constructible] (1)): it is a lisse $\mathcal O_{E,Y}$-module,
possibly with torsion. Extension of scalars along
the flat maps $\mathcal O_E\to E\to\Qlb$ is exact and commutes with $Rf_*$
([sk-prop-scalar-six], [det-prop-sfb-finite-extension-compatibility]), so
$R^{i}f_*\mathcal F\cong\Qlb\otimes_{\mathcal O_E}R^{i}f_*L_0$ is a lisse
$\overline{\mathbf Q}_{\ell,Y}$-module. Its stalks at geometric points over
closed points are computed by [cor-weil-pbc-geometric-fiber-qbar], and
compatibly with the Weil structures, after pulling back along
$\operatorname{Spec}\kappa(y)\to Y_0$, by [thm-weil-pbc-qbar] (2). This
completes (a).

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

*Step 3 (lower bound by fibrewise Poincaré duality).* Let
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

Now fix a closed point $y\in|Y_0|$ and $\bar y$ over it, and let
$X_{0,y}=X_0\times_{Y_0}\Spec\kappa(y)$ be the fibre, a smooth proper
$\kappa(y)$-scheme of pure dimension $d$ with geometric fibre $X_{\bar y}$;
here $\kappa(y)$ is a finite field with $q_y$ elements. The restriction of
$\mathcal F_0$ to $X_{0,y}$ is a lisse, hence perfect, Weil sheaf. The
degreewise duality over a field [thm-pod-degreewise-perfectness-over-a-field]
(with $H_c=H$, the fibre being proper) gives a perfect pairing

$$
H^{i}(X_{\bar y},\mathcal F)\times H^{2d-i}\bigl(X_{\bar y},\mathcal F^\vee(d)\bigr)
\longrightarrow\Qlb,
$$

and by [thm-pod-equivariance-of-the-twisted-pairing] it is invariant under
the geometric Frobenius of $\kappa(y)$ acting on both factors. By Step 1 and
[thm-weil-pbc-qbar] (2), these Frobenius operators are the local operators
$F_y$ on the stalks of $R^{i}f_{0*}\mathcal F_0$ and of
$R^{2d-i}f_{0*}(\mathcal F_0^\vee(d))$ at $\bar y$. An invariant perfect
pairing identifies the second factor with the contragredient of the first,
so the eigenvalues of $F_y$ on the second factor are the $\alpha^{-1}$, with
multiplicities, $\alpha$ running over the eigenvalues of $F_y$ on
$H^{i}(X_{\bar y},\mathcal F)$. Step 2 applied to the lisse, punctually pure
$\mathcal F_0^\vee(d)$ of weight $-w-2d$ in degree $2d-i$ bounds these by
$|\iota(\alpha^{-1})|\leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}$, i.e.

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
