+++
kind = "proof"
of = "theorem-trace-formula-frobenius-correspondence"
order = 1008
uses = ["proposition-w-local-components", "proposition-milnor-sequence", "theorem-comparison-direct-images", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "proposition-proper-base-change-etale-site", "definition-projection-formula-map", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "theorem-smooth-base-change-classical-torsion", "lemma-change-coefficients", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "proposition-properties-trace", "definition-correspondence", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "definition-trace-class-local-terms", "lemma-local-terms-point", "definition-action-correspondence", "definition-pushforward-correspondence", "theorem-proper-pushforward-lefschetz-verdier", "proposition-additivity-trace-classes", "lemma-frobenius-fixed-scheme", "proposition-frobenius-local-term-curve", "lemma-comparison-via-relative-frobenius", "lemma-additivity-open-subscheme-complement"]
+++
Both sides are defined, because the complexes are perfect by
Lemma [lemma-perfect-complexes-geometric-point]. We prove the assertion
simultaneously for all finite fields, all Frobenius correspondences and
all $m$, so that $\mathbf F_q$ may be replaced by $\mathbf F_{q^m}$
when we pass to a rational fibre. We go in four steps: finite schemes;
the affine line, where we use the Lefschetz–Verdier formula on
$\mathbf P^1$; closed subschemes of $\mathbf A^d$, by
projecting away one coordinate; and arbitrary $X_0$, by
cutting it into affine pieces.

*Finite schemes.* If $X_0$ is finite, both sides of the formula can
be read off from a block matrix. Indeed, up to nilpotents, $X$ is
the finite disjoint union of its geometric points. By nilpotent
invariance, $R\Gamma_c(X,K)=\bigoplus_{z\in X(k)}K_z$.
In this decomposition, the pullback along $\Phi_X^m$ given by the unit permutes these summands, and the block of $T_{c_m}(\psi_m)$ from $K_{\Phi_X^m(z)}$ to $K_z$ is
the stalk of $\psi_m$ at $z$, a map
$K_{\Phi_X^m(z)}=((\Phi_X^m)^*K)_z\to K_z$. On a finite projective model only the diagonal blocks
contribute to the trace. These occur exactly at the points
$z\in X_0(\mathbf F_{q^m})$, with the required stalk maps.

*The affine line.* This is the only step where we compute a local
term. We pass to $\mathbf P^1$, where the Lefschetz–Verdier formula
applies, and extend $K$ by zero, so that the new fixed point $\infty$
contributes nothing. Let $j:\mathbf A^1_k\hookrightarrow\mathbf P^1_k$.
The correspondence $\psi_m$ extends to a correspondence $\bar\psi_m$ on
$j_!K$, compatible with iteration. Indeed, $j$ is defined over $\mathbf F_q$,
so its square with the Frobenius maps is cartesian, and base change for this
square gives
$(\Phi_{\mathbf P^1}^m)^*j_!K\simeq j_!(\Phi_{\mathbf A^1}^m)^*K$.
Lemma [lemma-comparison-via-relative-frobenius](3), applied to $j$,
shows that the composition isomorphism

$$
R\Gamma_c(\mathbf A^1,K)
\simeq R\Gamma(\mathbf P^1,j_!K)
$$

intertwines the endomorphisms $T_{c_m}$ induced by $\psi$ and $\bar\psi$.
The graph is proper on the proper curve $\mathbf P^1$, so by
Theorem [theorem-proper-pushforward-lefschetz-verdier] the trace on the
right is the sum of the local terms at the fixed points.
By Proposition [proposition-frobenius-local-term-curve], each local term is a trace on a stalk. In particular, the local term at infinity vanishes, because
the stalk of $j_!K$ there is zero. The other fixed points and stalk
maps are those of $\mathbf A^1_{\mathbf F_q}$. This proves the formula for
the affine line.

*Closed subschemes of the affine line.* Let
$X_0=\operatorname{Spec}\mathbf F_q[t]/I$. If $I=0$, the
previous paragraph applies. Otherwise $I$ contains a nonzero polynomial,
so $X_0$ is finite over $\mathbf F_q$ and the case of finite schemes applies.
This also covers nonreduced subschemes.

*Induction on affine coordinates.* We push $K$ forward along a
coordinate projection. This does not change the global side. The
local side over a point of the base becomes the global side of a fibre
lying in $\mathbf A^1$. Suppose that the assertion holds
for closed subschemes of $\mathbf A^{d-1}$ over every finite field,
and let $X_0\hookrightarrow\mathbf A^d_{\mathbf F_q}$ be closed.
Let $f_0:X_0\to Y_0=\mathbf A^{d-1}_{\mathbf F_q}$ forget the last
coordinate, and let $f:X\to Y$ be its base change to $k$. The complex
$L=Rf_!K$ lies in $D^b_{\mathrm{ctf}}(Y,A)$ by
Proposition [proposition-six-operations-dctf], and we equip it with the
Frobenius correspondence $\psi'$ of
Lemma [lemma-comparison-via-relative-frobenius](2). As
Lemma [lemma-comparison-via-relative-frobenius](3) identifies the endomorphisms $T_{c_m}$,
the induction hypothesis shows that

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X,K))
=\sum_{y\in Y_0(\mathbf F_{q^m})}
\operatorname{tr}_A(\psi'_{m,\bar y}\mid L_{\bar y}).
$$

By Lemma [lemma-comparison-via-relative-frobenius](4), each summand is the
trace on the cohomology with compact support of the fibre $X_{0,y}$, a closed
subscheme of $\mathbf A^1_{\mathbf F_{q^m}}$. Here the endomorphism is given by the restriction of $\psi_m$ to the fibre and the first power of the
Frobenius over $\mathbf F_{q^m}$. The case of closed subschemes of the affine line then turns this summand into the sum of the traces on stalks
over $X_{0,y}(\mathbf F_{q^m})$. As $y$ varies, these sets partition
$X_0(\mathbf F_{q^m})$, which proves the affine case.

*General schemes.* Both sides are additive for a decomposition
into an open subscheme and its closed complement: the global side by
Lemma [lemma-additivity-open-subscheme-complement], and the local side because the
rational points split. It is therefore enough to cut $X_0$ into affine pieces. Choose a finite affine open cover
$U_1,\ldots,U_N$ of $X_0$, let $W_i=\bigcup_{j\leq i}U_j$ and
$V_i=W_i\setminus W_{i-1}$, with the reduced closed structure.
Each $V_i$ is closed in the affine $U_i$, hence affine, and it is
the closed complement of $W_{i-1}$ in $W_i$. Applying
Lemma [lemma-additivity-open-subscheme-complement] successively, we see that the traces add
over this stratification. The affine case applied to each $V_i$ now gives the
equality for all separated $X_0$ of finite type.
