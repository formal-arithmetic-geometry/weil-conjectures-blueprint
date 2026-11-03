+++
id = "prose-20-01"
kind = "hidden"
title = "Deligne's theorem in general"
order = 762
+++
The bound on a single curve (Theorem [sk-thm-wft-curve-middle-upper]) has to be
upgraded to Theorem [sk-cor-dl-general-complex]: for every separated morphism
of finite type $f$, the functor $Rf_!$ carries $D_{\leq w}(X_0)$ into
$D_{\leq w}(Y_0)$. The model is the computation of the cohomology of a
surface fibred over a curve. If $f:X_0\to Y_0$ has curves as fibres,
the Leray spectral sequence $H^a_c(Y,R^bf_!\overline{\mathbf Q}_\ell)\Rightarrow H^{a+b}_c(X,\overline{\mathbf Q}_\ell)$ reduces a bound on $X$ to the curve case twice: once
for the fibres, which bounds the stalks of $R^bf_!\overline{\mathbf Q}_\ell$ by $b$, and once
on the base, applied to the sheaves $R^bf_!\overline{\mathbf Q}_\ell$. In his first
proof [deligne74] Deligne used this with a Lefschetz pencil,
where the direct image in the middle degree is controlled by the
Picard–Lefschetz formula. Here the base can be arbitrary and the
sheaves on it are not explicit, so the argument has to work for every
sheaf at once. As explained in Section [sec-wdef-route], Noether normalization
over strata reduces an arbitrary $f$ to quasi-finite maps and
projections of relative affine lines
(Lemma [sk-l-dl-general-normalization]), so the essential case is a
smooth family of affine curves $h:U_0\to Y_0$ and a pure lisse sheaf $F$
on $U_0$.

Applied fibre by fibre, the curve case bounds each local eigenvalue of
$R^ih_!F$: at a closed point $y$ the stalk is $H^i_c(U_{\bar y},F)$,
which has weights at most $w+i$. This does not yet say that
$R^ih_!F$ has weights at most $w+i$ in the sense of
Definition [sk-d-real-weights], which asks for a finite filtration with
pure quotients. A filtration is what the next step needs: on the base,
$R^ih_!F$ is fed again into the curve case, which applies only to pure
lisse sheaves, and the bound for a mixed sheaf follows from those for
its pure quotients. Once a mixed filtration exists, the pointwise bound
bounds the weights of its quotients
(Lemma [sk-lem-wgen-punctual-cutoff]). So the problem is to show that the
direct images are mixed.

Mixedness comes from positivity again, through the following theorem
(Theorem [sk-i-dl-general-real]):

> every constructible real Weil sheaf on a separated scheme of finite
> type over $k_0$ is mixed.

For a lisse sheaf on a smooth affine $X_0$, the idea is to compare the
eigenvalues at a fixed point $x_*$ with those at an arbitrary point $x$
by a curve through both. On such a curve each constituent of the
restricted sheaf is pure by Theorem [sk-p-real-purity], so the
eigenvalues at $x$ have the weight read off at $x_*$. For this to show
anything about a constituent $S$ on $X_0$, the restriction of $S$ to the
curve must remain irreducible. Bertini's theorem provides such curves:
irreducibility is detected in one finite quotient of the fundamental
group (Lemma [sk-lem-wgen-finite-witness]), and a general complete
intersection curve through given points stays connected in the
corresponding finite étale cover (Lemma [sk-lem-wgen-bertini-cover] and
Corollary [sk-cor-wgen-bertini-irreducible]). Constructible sheaves are
then handled by stratifying.

To apply the theorem we need the direct images to be real. Replace $F$
by the real sheaf $G=F^0\oplus(F^0)^\vee$ of
Proposition [sk-prop-wrp-real-envelope], pure of weight zero, of which a
twist of $F$ is a summand. At a closed point $y$, the trace formula on
the fibre, together with $H^0_c(U_{\bar y},G)=0$ since the fibres are
affine, writes the real $L$-function of $G$ as

$$
L_\iota(U_y,G,T)=\frac{\iota P_{1,y}(T)}{\iota P_{2,y}(T)},
$$

where $P_{i,y}$ is the characteristic polynomial of Frobenius on
$H^i_c(U_{\bar y},G)$. The reciprocal roots of $P_{1,y}$ have absolute
value at most $q_y^{1/2}$ by the curve case, and those of $P_{2,y}$ have
absolute value $q_y$. Hence the two polynomials have no common root, and
since the reduced form of a real rational function is real, both
$\iota P_{1,y}$ and $\iota P_{2,y}$ have real coefficients. Thus the
direct images of $G$ are real, hence mixed, and so are those of $F$
(Theorem [sk-p-dl-general-relative-line]). Here the weight bound on curves
is used twice, once to separate $H^1_c$ from $H^2_c$ and once to bound
the quotients.

The reductions that remain are formal. Localization sequences on the
source and base change on the target reduce the bound for $R^if_!$ to
the pieces of finite partitions, the Leray spectral sequence shows that
the bound is stable under composition
(Theorem [sk-thm-dl-general-sheaf]), and the truncation spectral
sequence passes from sheaves to complexes. In
Section [sec-zeta-weil] the theorem gives the upper bound in the
purity of the cohomology of a smooth proper variety.
