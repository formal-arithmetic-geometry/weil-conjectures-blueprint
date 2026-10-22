# Tex changes proposed to match the blueprint and Lean: Picard appendix (2026-10-21)

Tex file: `DerivedCategoryAndSixFunctorsChoice_readable.tex`, Appendix "Picard schemes and Jacobians"
(lines about 19486–20065). Nothing in the tex was edited. Lean reference: `slopmaster2` at a762b776d6.

Part 1 lists the statements that the blueprint now states in Lean's (more general) form, with the tex passage that
states or uses the same fact and a proposed tex wording. Part 2 lists tex declarations whose blueprint sketch block
follows Lean and differs from the tex; the blueprint was **not** changed there (user decision), and the proposed
tex wording would bring the tex in line with the blueprint.

## Part 1: statements generalized in the blueprint to match Lean

### `def-pd-fibrewise-degree` / `def-pd-degree-morphism`

**Tex lines:** 19500-19512 (Definition [Relative Picard functor]); prose uses at 19813-19815, 19993-19995, 20004-20005

**Current tex:**

> No definition of the fibrewise degree or of deg: Pic -> Z in the tex. It is used only in prose: 'For a proper flat family of line bundles, the Euler characteristic of the fibres is locally constant. By Riemann--Roch, the degree is therefore locally constant as well' (19813-19815); 'Its degree-zero part is an open and closed algebraic subgroup space, because the degree is locally constant in families' (19993-19994); 'The fppf Picard sheaf and the fibrewise degree commute with field extension' (20004-20005).

**Proposed tex:**

> Insert after \end{definition} at 19512:
> \begin{definition}[Fibrewise degree and the degree morphism]
> Let $f:X\to S$ be proper and locally of finite presentation, $T$ an $S$-scheme and $\mathcal L$ invertible on $X_T$. For $t\in T$ the fibre $X_t$ of $X_T\to T$ is proper over $\kappa(t)$, and the fibrewise degree is
> \[\deg_T(\mathcal L)(t)=\chi(X_t,\mathcal L_t)-\chi(X_t,\mathcal O_{X_t}).\]
> If $f$ is moreover flat, then for $x\in\operatorname{Pic}_{X/S}(T)$ we put $\deg(x)(t)=\deg_Z(\mathcal L)(z)$ for any flat morphism $g:Z\to T$ locally of finite presentation, any $z\in Z$ over $t$ and any invertible $\mathcal L$ on $X_Z$ representing $g^*x$. This defines a morphism of fppf sheaves $\deg:\operatorname{Pic}_{X/S}\to\underline{\mathbf Z}$ to the sheaf of locally constant functions, and we put $\operatorname{Pic}^d_{X/S}=\deg^{-1}(d)$, $\operatorname{Pic}^0_{X/S}=\ker(\deg)$. Over a field $k$, $\operatorname{Pic}^d_{X/k}$ is also the fppf sheafification of the subpresheaf of classes all of whose pullbacks to $X_K$, for fields $K$ over $k$, have degree $d$.
> \end{definition}

**Why:** The tex defines deg only for C/k via Riemann-Roch; the blueprint (following Lean) defines it as a difference of fibre Euler characteristics for any proper lfp X->S, so Riemann-Roch is not needed for local constancy.

### `lem-pd-degree-locally-constant`

**Tex lines:** 19813-19816

**Current tex:**

> For a proper flat family of line bundles, the Euler characteristic of the fibres is locally constant. By Riemann--Roch, the degree is therefore locally constant as well, and this defines the displayed decomposition into open and closed pieces.

**Proposed tex:**

> Let $f:X\to S$ be proper, flat and locally of finite presentation. For an invertible sheaf $\mathcal L$ on $X_T$, the fibrewise degree $t\mapsto\chi(X_t,\mathcal L_t)-\chi(X_t,\mathcal O_{X_t})$ is locally constant on $T$, because near each point both Euler characteristics are computed by one bounded complex of finite free modules (coherent base change, as in Lemma~\ref{app:picard-coherent-base-change}). It is compatible with base change $T'\to T$ and with pullback to field-valued points, and it does not change when $\mathcal L$ is twisted by $f_T^*\mathcal N$ for an invertible $\mathcal N$ on $T$. Applied to $C\to\operatorname{Spec}k$, this defines the displayed decomposition into open and closed pieces.

**Why:** Lemma app:picard-coherent-base-change (19605-19614) is stated only for C/k and locally Noetherian T. The general statement needs the proper, finitely presented version (blueprint lem-pc-rf-perfect-base-change).

### `det-lem-picard-zero-dictionary` (zero-scheme dictionary)

**Tex lines:** 19703-19715 (proof of Proposition app:picard-abel-chart), under the standing hypotheses at 19569 and 19672

**Current tex:**

> Conversely, let $\mathcal L$ be a rigidified class in $F(T)$ and set $\mathcal N=f_{T,*}\mathcal L$. The evaluation map $f_T^*\mathcal N\to\mathcal L$ is a section of $\mathcal L\otimes f_T^*\mathcal N^{-1}$. On each geometric fibre it is a nonzero element of the one-dimensional space of sections, and hence its zero scheme $D$ is a relative effective Cartier divisor. For a point $t$ of $T$, Riemann--Roch shows that \[\deg\mathcal L_t=\chi(\mathcal L_t)-(1-g)=1-(1-g)=g.\] The divisor is proper with finite fibres and flat over $T$. Hence it is finite locally free of degree $g$, and it defines a morphism $T\to H_g$.

**Proposed tex:**

> Conversely, let $\mathcal L$ be a rigidified class in $F(T)$ and set $\mathcal N=f_{T,*}\mathcal L$. The evaluation map $f_T^*\mathcal N\to\mathcal L$ is a section $s$ of $\mathcal L\otimes f_T^*\mathcal N^{-1}$. This step uses no assumption on $k$ beyond the existence of $P$: on each fibre $C_{\kappa(t)}$, which is integral because $C$ is geometrically integral, $s$ is a nonzero element of the one-dimensional space of sections, so its zero scheme is an effective Cartier divisor of degree $\deg\mathcal L_t=\chi(\mathcal L_t)-(1-g)=1-(1-g)=g$ (Riemann--Roch), and the zero scheme $D$ of $s$ is a relative effective Cartier divisor on $C_T/T$, finite locally free of degree $g$ over $T$. It therefore defines a morphism $T\to H_g$.

**Why:** The tex already states the dictionary over a general field; only the blueprint had 'k separably closed'. The proposal makes the generality explicit, works on all fibres rather than geometric fibres, and uses geometric integrality.

### `lem-pd-group-scheme-descent`

**Tex lines:** 19988-20002 (proof of Proposition app:jacobian-ground-field)

**Current tex:**

> No group-scheme descent statement: the tex obtains the group structure from algebraic spaces: 'so the degree-zero subspace is a separated group algebraic space over $k$ with these properties. By the representability theorem for group algebraic spaces \stacks{0B8F} it is a scheme, which we denote by $J_0$'.

**Proposed tex:**

> (inside the replacement proof of item (iv)) 'The multiplication and unit of $J_s$ are compatible with the descent datum, since they come from the group structure of the functor $\operatorname{Pic}^0_{C_0/k}$. For a faithfully flat quasi-compact $X\to Y$, a group scheme over $X$ with an effective descent datum compatible with multiplication and unit carries a unique group scheme structure over $Y$ on the descended scheme whose base change is the given one; compatibility with the inverse is automatic, and commutativity descends. Hence $J_0$ is a commutative group scheme over $k$.'

**Why:** The tex has no counterpart. It enters only with the Galois-descent rewrite of item (iv).

### `lem-pc-degree-zero-properties`

**Tex lines:** 19612-19614 and 19703-19704

**Current tex:**

> 'On this locus, $f_{T,*}\mathcal L$ is invertible, its formation commutes with arbitrary base change, and $R^1f_{T,*}\mathcal L=0$.' (19612-19614); '...and set $\mathcal N=f_{T,*}\mathcal L$.' (19703-19704)

**Proposed tex:**

> At 19703-19704: '...and set $\mathcal N=f_{T,*}\mathcal L=H^0(Rf_{T,*}\mathcal L)$. Since $Rf_{T,*}\mathcal L\simeq\mathcal N'[0]$ for an invertible $\mathcal N'$, we have $\mathcal N\simeq\mathcal N'$ and $R^if_{T,*}\mathcal L=0$ for $i\neq0$; indeed, in the derived category of any abelian category an object isomorphic to $E[-n]$ has $H^n\simeq E$ and no other cohomology.'

**Why:** The tex uses this fact without stating it. It is optional to add it.

### `prop-pc-xk-integral`

**Tex lines:** 19560-19564 (and implicitly 19743, 19569-19572)

**Current tex:**

> For a smooth proper geometrically connected curve $C$ over a field $k$, we have $H^0(C,\mathcal O_C)=k$. Since every $k$-scheme is flat over $k$, flat base change for coherent cohomology shows that $(\ast)$ holds for $C\to\operatorname{Spec}k$. If $C$ has a $k$-point $P$, the preceding lemma applies with $\sigma=P$ (see \stacks{0B9U}).

**Proposed tex:**

> Let $C$ be a smooth proper geometrically connected curve over a field $k$ (over a separably closed $k$ it suffices that $C$ be connected). Then $H^0(C,\mathcal O_C)=k$. For every field extension $K/k$ the base change $C_K$ is integral, smooth of relative dimension $1$ and proper over $K$, with $H^0(C_K,\mathcal O_{C_K})=K$ and $\dim_KH^1(C_K,\mathcal O_{C_K})=\dim_kH^1(C,\mathcal O_C)$, by flat base change for coherent cohomology. Since every $k$-scheme is flat over $k$, the same flat base change shows that $(\ast)$ holds for $C\to\operatorname{Spec}k$. If $C$ has a $k$-point $P$, the preceding lemma applies with $\sigma=P$ (see \stacks{0B9U}).

**Why:** The tex never claims that C_K is projective. The projectivity claim came only from the blueprint and has been removed. Line 19743 ('the section has a finite zero divisor on $C_K$') relies on the integrality of C_K that this paragraph now states.


## Part 2: tex declarations where the blueprint follows Lean (blueprint unchanged for now)

### app:picard-riemann-roch (block sk-thm-picard-rr)

**Tex lines:** 19569-19572 (standing hypothesis), 19574-19590 (theorem), 19592-19598 (justification)

**Current tex:**

> Fix a smooth projective geometrically connected curve $C/k$, and set $g=\dim_kH^1(C,\mathcal O_C)$. Smooth proper geometrically connected curves over a field are projective \stacks{0A26}, and hence this includes the proper curves of the main text. ... These identifications commute with field extension. ... This is coherent duality and the Riemann--Roch theorem for smooth curves \stacks{0B5B}, where the duality is given by the residue trace on differentials.

**Proposed tex:**

> 19569-19572: 'Fix a smooth proper curve $C/k$ with $H^0(C,\mathcal O_C)=k$, and set $g=\dim_kH^1(C,\mathcal O_C)$. For smooth proper $C$ the condition $H^0(C,\mathcal O_C)=k$ is equivalent to geometric connectedness, and such curves are projective \stacks{0A26}; hence this includes the proper curves of the main text.' In the theorem replace 'These identifications commute with field extension.' by 'The genus and the degree are invariant under extension of the ground field, and $C_K$ again satisfies the hypotheses.' Replace the justification by: 'Here $\deg\mathcal L=\sum_xn_x[\kappa(x):k]$ for any divisor $D=\sum_xn_xx$ with $\mathcal L\simeq\mathcal O_C(D)$. Since coherent cohomology vanishes in degrees $\ge2$, $\chi=h^0-h^1$, and the sequence $0\to\mathcal O_C(D-x)\to\mathcal O_C(D)\to\kappa(x)\to0$ gives $\chi(\mathcal O_C(D))=\chi(\mathcal O_C(D-x))+[\kappa(x):k]$. Induction on $\sum_x|n_x|$ gives $\chi(\mathcal L)=\deg\mathcal L+\chi(\mathcal O_C)$, and $\chi(\mathcal O_C)=1-g$ because $H^0(C,\mathcal O_C)=k$. Coherent duality is \stacks{0B5B}, with the residue trace on differentials. Duality with $\mathcal L=\mathcal O_C$ gives $\deg\omega_{C/k}=(g-1)-(1-g)=2g-2$. Flat base change $H^i(C_K,\mathcal L_K)=H^i(C,\mathcal L)\otimes_kK$ gives the invariance of $\chi$, the degree and the genus, and $H^0(C_K,\mathcal O_{C_K})=K$.' (Keep the vanishing paragraph.)

**Why:** The blueprint differs in three ways. (a) Its hypothesis is H^0(C,O_C)=k instead of 'projective geometrically connected'. (b) The field-extension clause is weakened from 'the identifications commute with field extension' to 'genus and degree are invariant'. (c) It proves Riemann-Roch by induction on divisors and only cites duality, via its sk-thm-picard-duality. The block also adds complements that the tex lacks: RR for coherent F, (G) positive degree implies ample, (H) the complement of an ample effective divisor is affine. These are used for the Hilbert scheme hypothesis. The standing sentence at 19569 also governs Subsections app:picard-coherent-tools and app:picard-hilbert, so changing it changes their hypothesis.

### app:picard-hilbert-theorem (block sk-thm-picard-hilb-curves)

**Tex lines:** 19644-19652 (theorem), 19654-19656 (route)

**Current tex:**

> Representability and properness follow from the Hilbert scheme of points on a smooth proper curve \stackss{0B9A}{0B9I}. We verify the remaining properties.

**Proposed tex:**

> Representability follows from the general representability of Hilbert functors of points: for a separated morphism $X\to S$ such that any finitely many points of a fibre lie in an affine open of $X$, the functor $\operatorname{Hilb}^d_{X/S}$ is representable by a scheme (compare \stackss{0B9A}{0B9I}). For $C/k$ this hypothesis follows from Riemann--Roch: an effective divisor $D_0$ through the given points has positive degree, so $\mathcal O_C(D_0)$ is ample and $C\setminus\operatorname{Supp}D_0$ is affine. The addition map $C^d\to H_d$ is finite locally free and surjective, so $H_d$ is proper, being the image of the proper $C^d$. We verify the remaining properties. [Optionally append to the theorem: 'For a field extension $k'/k$ the $k'$-points of $H_d$ are the effective Cartier divisors of degree $d$ on $C_{k'}$, and there are addition morphisms $H_{d_1}\times_kH_{d_2}\to H_{d_1+d_2}$, finite locally free of degree $\binom{d_1+d_2}{d_1}$.']

**Why:** The blueprint routes representability through sk-thm-picard-hilb-general (Lean isRepresentable_hilbertPresheaf) and checks the affine-open hypothesis with sk-thm-picard-rr (G)+(H). It also gives an alternative smoothness proof by induction through the addition morphism. Discrepancy: the block statement says H_d is 'smooth projective geometrically integral', while the tex says 'proper' and Lean hilbertPresheaf_curve_representable proves smooth, proper and geometrically integral, not projective. Keep 'proper' in the tex. The block should probably be changed to 'proper'.

### app:jacobian-ground-field (block sk-prop-jacobian-descent)

**Tex lines:** 19973-19986 (statement), 19988-20002 (algebraic-space construction), 20004-20015

**Current tex:**

> Statement: 'Let $C_0/k$ be a smooth proper geometrically connected curve, and put $C=C_0\times_k\bar k$. There is an abelian variety $J_0/k$ representing the degree-zero relative Picard fppf sheaf of $C_0$. Its base change represents $\operatorname{Pic}^0_{C/\bar k}$, and the canonical identification $J_0(\bar k)=\operatorname{Pic}^0(C)$ is Galois-equivariant.' Proof (19989-20002): 'Since $C_0$ is flat, proper and of finite presentation over $k$, ... the fppf Picard sheaf of $C_0$ is an algebraic space by \stacks{0D2C}. Its degree-zero part is an open and closed algebraic subgroup space ... By the representability theorem for group algebraic spaces \stacks{0B8F} it is a scheme, which we denote by $J_0$, and $J_0$ is an abelian variety.'

**Proposed tex:**

> Statement: 'Let $C_0/k$ be a smooth proper geometrically connected curve of genus $g$, let $k_s\subseteq\bar k$ be a separable closure, and put $C=C_0\times_k\bar k$. There is an abelian variety $J_0/k$ of dimension $g$ representing $\operatorname{Pic}^0_{C_0/k}=\ker(\deg)$. For every field extension $K/k$, $J_0\times_kK$ represents $\operatorname{Pic}^0_{C_{0,K}/K}$, naturally in $K$, and the identification $J_0(\bar k)=\operatorname{Pic}^0(C)$ is $\operatorname{Gal}(k_s/k)$-equivariant; in particular so is $J_0[\ell^n](\bar k)\simeq\operatorname{Pic}^0(C)[\ell^n]$.' Proof replacing 19989-20002: 'Over $k_s$ the curve $C_{k_s}$ has a $k_s$-point, so Theorem~\ref{app:picard-curve}, whose proof only uses that the ground field is separably closed, gives an abelian variety $J_s$ representing $\operatorname{Pic}^0_{C_{k_s}/k_s}$. Since $\operatorname{Pic}^0_{C_0/k}$ is a functor on $k$-schemes, the two pullbacks of $J_s$ to $k_s\otimes_kk_s$ represent the same functor, and Yoneda gives a canonical descent datum on $J_s$ relative to $k_s/k$. $J_s$ is projective and of finite presentation, so by limit arguments \stacks{01ZM} the datum is already defined on a projective $J_1$ over a finite Galois extension $k_1/k$. Descent along the finite locally free $k_1/k$ is effective for projective schemes \stacks{0CCJ}, which gives $J_0$ over $k$. The multiplication and unit are compatible with the datum, so they descend and $J_0$ is a group scheme. Properness, smoothness, geometric connectedness and dimension descend along $k_s/k$. Because $\operatorname{Pic}^0_{C_0/k}$ is limit preserving and an fppf sheaf, the representing isomorphism over $k_s$ descends to $h_{J_0}\simeq\operatorname{Pic}^0_{C_0/k}$.' (Keep 20004-20015 for the base-change comparisons and equivariance.)

**Why:** The blueprint avoids algebraic spaces (0D2C, 0B8F). It builds J over k_s by the rigidified construction (thm-pc-picard-representable is stated for separably closed fields), then uses Galois/fpqc descent: canonical Yoneda descent datum, the finite level k_1 via limits, effective descent for projective schemes, descent of the group law, and descent of the representing isomorphism. The sketch also explains why a rational point over a finite extension is not enough: over F_2, y^2+y=x^5+x^3+1 has no twist into the chart. The statement adds 'J_K represents Pic^0_{C_K/K} for every K' and the ell^n-torsion equivariance. Its Galois group is Gal(k_s/k), where the tex has Gal(bar k/k) (these coincide via restriction). Theorem app:picard-curve is stated for algebraically closed k, so the proposal needs its separably closed version (tex 19767-19770). The blueprint's thm-pc-picard-representable/sk-thm-picard-main covers that.


## Related blueprint changes already made (no tex change needed)

- `sk-thm-picard-hilb-curves`: the block said H_d is "smooth projective"; it now says "smooth proper", as the tex
  (`app:picard-hilbert-theorem`) and Lean (`hilbertPresheaf_curve_representable`) do.
- `sk-thm-picard-perfect` (`app:picard-coherent-base-change`): back to the tex's derived form
  (La^*Rf_{T,*}L → Rf_{T',*}L_{T'} an isomorphism in the derived category).
