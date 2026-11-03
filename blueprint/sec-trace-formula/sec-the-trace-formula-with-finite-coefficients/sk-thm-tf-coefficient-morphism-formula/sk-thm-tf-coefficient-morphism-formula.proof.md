+++
kind = "proof"
of = "sk-thm-tf-coefficient-morphism-formula"
uses = ["sk-lem-tf-compact-trace", "sk-i-relative-frob", "sk-p-proper", "sk-p-frob", "sk-thm-sf-ctf-stability", "sk-i-global-additivity", "sk-lem-finite"]
+++
The complexes are perfect by Lemma [sk-lem-finite]. We prove the assertion
simultaneously for all finite fields, all Frobenius correspondences and
all $m$, so that $\mathbf F_q$ may be replaced by $\mathbf F_{q^m}$
when we pass to a rational fibre.

*Finite schemes.* If $X_0$ is finite, then up to nilpotents $X$ is
the finite disjoint union of its geometric points, so by nilpotent
invariance $R\Gamma_c(X,K)=\bigoplus_{z\in X(k)}K_z$.
The pullback along $\Phi_X^m$ given by the unit permutes these summands, and
$T_{c_m}(\psi_m)$ has block from $K_{\Phi_X^m(z)}$ to $K_z$ equal to
the stalk of $\psi_m$ at $z$, a map
$K_{\Phi_X^m(z)}=((\Phi_X^m)^*K)_z\to K_z$. On a finite projective model only the diagonal blocks
contribute to the trace, and these occur exactly at the points
$z\in X_0(\mathbf F_{q^m})$, with the required stalk maps.

*The affine line.* Let $j:\mathbf A^1_k\hookrightarrow\mathbf P^1_k$.
Since $j$ is defined over $\mathbf F_q$, its square with the
Frobenius maps is cartesian. Base change for this square shows that
$(\Phi_{\mathbf P^1}^m)^*j_!K\simeq j_!(\Phi_{\mathbf A^1}^m)^*K$, and
we obtain an extension
$\bar\psi_m$ of $\psi_m$ to $j_!K$, compatible with iteration. The
composition isomorphism

$$
R\Gamma_c(\mathbf A^1,K)
\simeq R\Gamma(\mathbf P^1,j_!K)
$$

intertwines the endomorphisms $T_{c_m}$ induced by $\psi$ and $\bar\psi$, by
Lemma [sk-i-relative-frob](3) applied to $j$. On
the proper curve $\mathbf P^1$ the graph is proper, so by
Theorem [sk-p-proper] the trace is the sum of
the local terms at the fixed points. By
Proposition [sk-p-frob], each local term
is a trace on a stalk. Since the stalk of $j_!K$ at infinity is zero, the
local term at infinity vanishes, and the other fixed points and stalk maps are those of
$\mathbf A^1_{\mathbf F_q}$. This proves the formula for the affine line.

*Closed subschemes of the affine line.* Let
$X_0=\operatorname{Spec}\mathbf F_q[t]/I$. Either $I=0$ and the
previous paragraph applies, or $I$ contains a nonzero polynomial, so that
$X_0$ is finite over $\mathbf F_q$ and the case of finite schemes applies
(also to nonreduced subschemes).

*Induction on affine coordinates.* Suppose that the assertion holds
for closed subschemes of $\mathbf A^{d-1}$ over every finite field,
and let $X_0\hookrightarrow\mathbf A^d_{\mathbf F_q}$ be closed.
Let $f_0:X_0\to Y_0=\mathbf A^{d-1}_{\mathbf F_q}$ forget the last
coordinate, and let $f:X\to Y$ be its base change to $k$. By
Proposition [sk-thm-sf-ctf-stability], $L=Rf_!K$ lies in
$D^b_{\mathrm{ctf}}(Y,A)$, and we equip it with the Frobenius correspondence $\psi'$ of
Lemma [sk-i-relative-frob](2). Since
Lemma [sk-i-relative-frob](3) identifies the endomorphisms $T_{c_m}$,
the induction hypothesis shows that

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X,K))
=\sum_{y\in Y_0(\mathbf F_{q^m})}
\operatorname{tr}_A(\psi'_{m,\bar y}\mid L_{\bar y}).
$$

The fibre $X_{0,y}$ is a closed subscheme of
$\mathbf A^1_{\mathbf F_{q^m}}$. By Lemma [sk-i-relative-frob](4),
each summand is the trace on its cohomology with compact support, for the
restriction of $\psi_m$ to the fibre and the first power of the Frobenius over
$\mathbf F_{q^m}$. By the case of closed subschemes of the affine line,
this is the sum of the traces on stalks over
$X_{0,y}(\mathbf F_{q^m})$. These sets partition
$X_0(\mathbf F_{q^m})$ as $y$ varies, which proves the affine case.

*General schemes.* Choose a finite affine open cover
$U_1,\ldots,U_N$ of $X_0$, let $W_i=\bigcup_{j\leq i}U_j$ and
$V_i=W_i\setminus W_{i-1}$, with the reduced closed structure.
Each $V_i$ is closed in the affine $U_i$, hence affine, and it is
the closed complement of $W_{i-1}$ in $W_i$. Applying
Lemma [sk-i-global-additivity] successively, we see that the traces add
over this stratification. Since the sums over points add as well, the
equality follows from the affine case.
