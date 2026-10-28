+++
kind  = "proof"
of    = "prop-trf-trace-formal-laws"
+++
In this proof all traces are the categorical traces of
[def-trf-categorical-trace], computed with the explicit model
conventions of [lem-trf-chain-supertrace]; throughout, $w^\vee$
denotes the natural isomorphism
$R\operatorname{Hom}_A(w,A):P_2^\vee\xrightarrow{\sim}P_1^\vee$ induced
by an isomorphism $w:P_1\xrightarrow{\sim}P_2$ (the internal Hom is a
bifunctor of the derived category, [def-weil-derived-tensor]).

*(1) Conjugacy invariance.* The duality data
$\operatorname{coev}_{P_i},\operatorname{ev}_{P_i}$ are natural in
isomorphisms: the squares

$$
\begin{array}{ccc}
A & \xrightarrow{\operatorname{coev}_{P_1}} & P_1\otimes^LP_1^\vee\\
\| & & \downarrow w\otimes^L(w^\vee)^{-1}\\
A & \xrightarrow{\operatorname{coev}_{P_2}} & P_2\otimes^LP_2^\vee
\end{array}
\qquad
\begin{array}{ccc}
P_1^\vee\otimes^LP_1 & \xrightarrow{\operatorname{ev}_{P_1}} & A\\
\downarrow (w^\vee)^{-1}\otimes^Lw & & \|\\
P_2^\vee\otimes^LP_2 & \xrightarrow{\operatorname{ev}_{P_2}} & A
\end{array}
$$

commute, and the braiding
$\operatorname{sim}$ is natural in both variables; these are the
compatibilities of the tensor–internal-Hom adjunction and of the
symmetric monoidal structure with the identification
$P^\vee=R\operatorname{Hom}_A(P,A)$. Hence, if
$v_2\circ w=w\circ v_1$, then with the abbreviations
$\iota_w=w\otimes^L(w^\vee)^{-1}$ and
$\iota^w=(w^\vee)^{-1}\otimes^Lw$:

$$
\begin{aligned}
\operatorname{tr}_A(v_2\mid P_2)
&=\operatorname{ev}_{P_2}\circ\operatorname{sym}\circ
(v_2\otimes^L1)\circ\operatorname{coev}_{P_2}\\
&=\operatorname{ev}_{P_2}\circ\operatorname{sym}\circ
\iota_w\circ(v_1\otimes^L1)\circ\operatorname{coev}_{P_1}\\
&=\operatorname{ev}_{P_1}\circ\operatorname{sym}\circ
(v_1\otimes^L1)\circ\operatorname{coev}_{P_1}
=\operatorname{tr}_A(v_1\mid P_1),
\end{aligned}
$$

where the second equality uses $v_2\otimes^L1=\iota_w\circ(v_1\otimes^L1) \circ\iota_w^{-1}$ together with the first square, and the third the
naturality of $\operatorname{sym}$ and the second square.

*(2) Filtered additivity.* This is the additivity of the trace on the
filtered derived category of perfect complexes,
[Stacks, Tag 03TJ](https://stacks.math.columbia.edu/tag/03TJ). Concretely,
an object of $DF(A)$ with a two-step filtration and perfect graded pieces is
represented by a filtered bounded complex of finite projective modules
$M'\subset M$ with $M'$ and $M''=M/M'$ bounded complexes of finite
projectives (the sequence $0\to M'\to M\to M''\to0$ is then degreewise
split), and a morphism in $DF(A)$ between such filtered complexes is
represented by a strict morphism of filtered complexes (filtered
quasi-isomorphisms are inverted, and a filtered map out of a filtered
complex of projectives with projective graded pieces lifts along a filtered
quasi-isomorphism). A strict endomorphism $\bar v$ of $M'\subset M$ is, in
degree $n$ and for a splitting $M^n=M'^n\oplus M''^n$, block triangular,

$$
\bar v^n=\begin{pmatrix}\beta^n & s^n\\ 0 & \alpha^n\end{pmatrix},
$$

with $\beta$ the restricted chain endomorphism of $M'$, which represents
$v'$, $\alpha$ the induced chain endomorphism of $M''$, which represents
$v''$, and $s^n:M''^n\to M'^n$ some family of maps. The trace of a
block-triangular matrix is the sum of the traces of its diagonal blocks, so
by the chain-level formula of [lem-trf-chain-supertrace]

$$
\begin{gathered}
\operatorname{tr}_A(v\mid P)
=\sum_i(-1)^i\operatorname{Tr}(\bar v^i\mid M^i)\\
=\sum_i(-1)^i\operatorname{Tr}(\beta^i\mid M'^i)
+\sum_i(-1)^i\operatorname{Tr}(\alpha^i\mid M''^i)
=\operatorname{tr}_A(v'\mid P')+\operatorname{tr}_A(v''\mid P''),
\end{gathered}
$$

the traces being independent of the chosen representatives by (1) and
[lem-trf-chain-supertrace]. The flaw of the naive argument for an
arbitrary endomorphism $(v',v,v'')$ of the triangle in the plain derived
category is visible here: one then only knows that $v$ is represented by a
chain map $M\to M$ whose squares with $M'\to M$ and $M\to M''$ commute up
to homotopy, and such a map need not be block triangular with diagonal
blocks representing $v'$ and $v''$. In Ferrand's example above every chain
representative of $v$ acts on the subcomplex $M'=R[-1]$ by $2$, which
represents $2\neq v'=0$ (the square commutes only up to the homotopy
$\mathrm{id}:M'^1\to M^0$), and the supertraces differ by $-2$.

*(3) Scalar extension.* The derived scalar extension
$F=-\otimes_A^LB:D(A)\to D(B)$ is exact (it is the derived tensor
product with the $K$-flat complex $B$) and monoidal: the canonical
comparison isomorphism

$$
F(P)\otimes_B^LF(Q)=(P\otimes_A^LB)\otimes_B^L(Q\otimes_A^LB)
\xrightarrow{\ \sim\ }(P\otimes_A^LQ)\otimes_A^LB=F(P\otimes_A^LQ)
$$

is the associativity of the derived tensor product (no flatness of
$B$ over $A$ is needed in the derived setting, as both sides
compute the same absolute derived tensor $P\otimes_A^LQ\otimes_A^LB$),
and it is compatible with the braidings, with the shifts, and with
distinguished triangles. It also carries the duals: the canonical
isomorphism

$$
F(P)^\vee=R\operatorname{Hom}_B(P\otimes_A^LB,B)
\xrightarrow{\ \sim\ }R\operatorname{Hom}_A(P,A)\otimes_A^LB=F(P^\vee)
$$

(the standard base-change statement for finite projective modules,
with the derived-tensor form valid for all $P\in D^b_{\mathrm{fin}}(A)$
via the projective resolution), and it identifies
$\operatorname{coev}_{F(P)}$, $\operatorname{ev}_{F(P)}$,
and the braiding with the $F$-images of
$\operatorname{coev}_P,\operatorname{ev}_P$ and the braiding;
consequently the composite of
[def-trf-categorical-trace] for $F(P)$ is the $F$-image
of the composite for $P$, and identifying
$\operatorname{End}_{D(B)}(B)\cong B$ with the application of
$\rho:\operatorname{End}_{D(A)}(A)\cong A\to B$ gives
$\rho(\operatorname{tr}_A(v\mid P))= \operatorname{tr}_B(v\otimes_A^LB\mid P\otimes_A^LB)$.
The same argument applies to the scalar extensions
$A\to A_{E'\!,n'}$, $A\to\mathcal O_E$, $\mathcal O_E\to E$, and
$E\to\Qlb$ between the coefficient rings: on perfect complexes over the
point these are the derived extensions of scalars along maps of condensed
rings of [det-def-sfb-coefficient-change], which are monoidal.

*(4) Supertrace over a field.* Let $\Lambda\in\{E,\Qlb\}$ (for
$\Lambda=E$, $D^b_{\mathrm{fin}}(E)$ is the bounded derived category
of finite-dimensional $E$-vector spaces by
[def-weil-finite-coefficient-point]). Every
$P\in D^b_{\mathrm{fin}}(\Lambda)$ is represented by a bounded
complex $P^\bullet$ of finite-dimensional $\Lambda$-vector spaces
together with a chain map $v^\bullet$ inducing $v$. For an integer
$i$ let $P^{\leq i}$ be the canonical truncation

$$
P^{\leq i}=\bigl(\cdots\to P^{i-2}\to P^{i-1}\to\ker d^i\to0\bigr)
$$

(a subcomplex stable under $v^\bullet$), so that
$P^{\leq i+1}/P^{\leq i}$ is the two-term complex

$$
C_i=\bigl(\operatorname{im}d^i\xrightarrow{d}\ker d^{i+1}\bigr)
\qquad\text{(degrees }i,i+1\text{)}
$$

with the induced endomorphism; it carries the induced endomorphism
and is quasi-isomorphic to
$\mathcal H^{i+1}(P)[-(i+1)]$ because the arrow
$\operatorname{im}d^i\hookrightarrow\ker d^{i+1}$ is injective with
cokernel $\mathcal H^{i+1}(P)$. Since all terms are vector spaces,
the short exact sequences

$$
0\to P^{\leq i}\to P^{\leq i+1}\to C_i\to0
$$

are degreewise split short exact sequences of complexes with strictly
compatible chain endomorphisms, hence give distinguished triangles of
$D^b_{\mathrm{fin}}(\Lambda)$ with endomorphisms of filtered origin in the
sense of (2). By (2), and by the chain-level computation of
[lem-trf-chain-supertrace] applied to $C_i$,

$$
\begin{aligned}
\operatorname{tr}_\Lambda(v\mid P^{\leq i+1})
&=\operatorname{tr}_\Lambda(v\mid P^{\leq i})
+\operatorname{tr}_\Lambda(v\mid C_i)\\
&=\operatorname{tr}_\Lambda(v\mid P^{\leq i})
+(-1)^i\operatorname{Tr}\bigl(v\mid\operatorname{im}d^i\bigr)
+(-1)^{i+1}\operatorname{Tr}\bigl(v\mid\ker d^{i+1}\bigr)\\
&=\operatorname{tr}_\Lambda(v\mid P^{\leq i})
+(-1)^{i+1}\operatorname{Tr}
\bigl(\mathcal H^{i+1}(v)\mid\mathcal H^{i+1}(P)\bigr),
\end{aligned}
$$

the last equality using the split exact sequence
$0\to\operatorname{im}d^i\to\ker d^{i+1}\to\mathcal H^{i+1}(P)\to0$
of vector spaces with the induced endomorphisms, which gives
$\operatorname{Tr}(v\mid\ker d^{i+1})- \operatorname{Tr}(v\mid\operatorname{im}d^i)= \operatorname{Tr}(\mathcal H^{i+1}(v))$. Induction over the finite
cohomological range of $P^\bullet$ (starting from
$P^{\leq i}=0$ below the lowest degree) gives

$$
\operatorname{tr}_\Lambda(v\mid P)
=\sum_{i\in\mathbf Z}(-1)^i\operatorname{Tr}
\bigl(\mathcal H^{i}(v)\mid\mathcal H^{i}(P)\bigr),
$$

which is the displayed formula.
