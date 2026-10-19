+++
kind = "proof"
of = "sk-thm-tf-coefficient-morphism-formula"
uses = ["sk-lem-tf-compact-trace", "sk-i-relative-frob", "sk-p-proper", "sk-p-frob", "sk-thm-sf-ctf-stability", "sk-i-global-additivity"]
+++
The proof first treats finite schemes and the affine line, the
latter by the Lefschetz–Verdier formula on $\mathbf P^1$ and the
curve local term. Pushforward along a coordinate projection then
reduces closed subschemes of $\mathbf A^d$ to fibres in $\mathbf A^1$,
and open–closed additivity reduces general $X_0$ to affine pieces;
the only compactification used is $\mathbf A^1\subset\mathbf P^1$.
The geometric content lies in the case of the affine line, through
the local term of [sk-p-frob]; the
other steps are formal reductions.

Perfectness is [sk-lem-tf-compact-trace]. We prove the assertion
simultaneously for all finite fields, all Frobenius correspondences and
all $m$, so that $\mathbf F_q$ may be replaced by $\mathbf F_{q^m}$
when we pass to a rational fibre.

*Finite schemes.* If $X_0$ is finite, nilpotent invariance and
the finite disjoint union of its geometric points give
$R\Gamma_c(X,K)=\bigoplus_{z\in X(k)}K_z$.
The unit pullback along $\Phi_X^m$ permutes these summands, and
$T_{c_m}(\psi_m)$ has block from $K_{\Phi_X^m(z)}$ to $K_z$ equal to
$\psi_{m,z}$. On a finite projective model only the diagonal blocks
contribute to the trace. They occur exactly at the points
$z\in X_0(\mathbf F_{q^m})$, with the required stalk maps.

*The affine line.* Let $j:\mathbf A^1_k\hookrightarrow\mathbf P^1_k$.
Since $j$ is defined over $\mathbf F_q$, its square with the
Frobenius maps is Cartesian, and base change for this open square gives
$(\Phi_{\mathbf P^1}^m)^*j_!K\simeq j_!(\Phi_{\mathbf A^1}^m)^*K$, and hence an extension
$\bar\psi_m$ of $\psi_m$ to $j_!K$, compatible with iteration. The
composition isomorphism

$$
 R\Gamma_c(\mathbf A^1,K)
 \simeq R\Gamma(\mathbf P^1,j_!K)
$$

intertwines the global operators of $\psi$ and $\bar\psi$, by the unit
compatibility in the open base-change square or by
[sk-i-relative-frob] (3) for $j$. On
the proper curve $\mathbf P^1$ the graph is proper, so
[sk-p-proper] writes the trace as the sum of
the local terms at the fixed points, and
[sk-p-frob] identifies each local term
with a stalk trace. The stalk of $j_!K$ at infinity is zero, so that
term vanishes; the other fixed points and stalk maps are those of
$\mathbf A^1_0$.

*Closed subschemes of the affine line.* For
$X_0=\operatorname{Spec}\mathbf F_q[t]/I$, either $I=0$ and the
previous paragraph applies, or a nonzero polynomial in $I$ makes
$X_0$ finite over $\mathbf F_q$, and the finite-scheme case applies,
also to nonreduced subschemes.

*Induction on affine coordinates.* Suppose the assertion holds
for closed subschemes of $\mathbf A^{d-1}$ over every finite field,
and let $X_0\hookrightarrow\mathbf A^d_{\mathbf F_q}$ be closed.
Let $f_0:X_0\to Y_0=\mathbf A^{d-1}_{\mathbf F_q}$ forget the last
coordinate, and let $f:X\to Y$ be its base change to $k$. By
[sk-thm-sf-ctf-stability], $L=Rf_!K$ lies in
$\Dctf(Y,A)$; equip it with the Frobenius correspondence $\psi'$ of
[sk-i-relative-frob] (2). Since
[sk-i-relative-frob] (3) identifies the global operators,
the induction hypothesis gives

$$
 \operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X,K))
 =\sum_{y\in Y_0(\mathbf F_{q^m})}
      \operatorname{tr}_A(\psi'_{m,\bar y}\mid L_{\bar y}).
$$

By [sk-i-relative-frob] (4) each summand is the compact
trace on the fibre $X_{0,y}$, a closed subscheme of
$\mathbf A^1_{\mathbf F_{q^m}}$, for the Frobenius correspondence
$\psi_m$ restricted to the fibre and the one-step Frobenius over
$\mathbf F_{q^m}$. The case of the affine line
identifies it with the sum of the stalk traces over
$X_{0,y}(\mathbf F_{q^m})$, and these sets partition
$X_0(\mathbf F_{q^m})$ as $y$ varies. This proves the affine case.

*General schemes.* Choose a finite affine open cover
$U_1,\ldots,U_N$ of $X_0$, let $W_i=\bigcup_{j\leq i}U_j$ and
$V_i=W_i\setminus W_{i-1}$, with the reduced closed structure.
Each $V_i$ is closed in the affine $U_i$, hence affine, and it is
the closed complement of $W_{i-1}$ in $W_i$. Applying
[sk-i-global-additivity] successively, the traces add
over this stratification, as do the point sums, and the affine case
gives the equality.

The detailed form of this argument is
[thm-trf-coefficient-morphism-trace-formula]; the extension to
$\mathbf P^1$ in the case of the affine line is
[lem-trf-compactification-cohomology] and
[lem-trf-compactification-graph-operator].
