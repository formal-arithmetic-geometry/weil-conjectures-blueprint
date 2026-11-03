+++
kind  = "proof"
of    = "det-thm-rationality"
+++
*Separated case.* If $X_0$ is separated, [sk-cor-tf-point-counting] gives
$Z(X_0,T)\in\Q(T)\cap(1+T\Z[[T]])$: the closed-point product has integer
coefficients, and rationality over $\Ql$ (from the determinant formula on
compactly supported cohomology) descends to $\Q$.

*General case.* Since $X_0$ is quasi-compact, it is covered by finitely many
affine opens $U_1,\dots,U_n$. The locally closed subsets
$V_j=U_j\setminus(U_1\cup\dots\cup U_{j-1})$, with their reduced structures,
partition $X_0$, and each $V_j$ is a locally closed subscheme of the affine
finite-type scheme $U_j$, hence separated and of finite type. A
$k_0$-morphism $\Spec\Fqn\to X_0$ is the same as a closed point $x$ with a
$k_0$-embedding $\kappa(x)\hookrightarrow\Fqn$, and $x$ lies in exactly one
$V_j$, with the same residue field; hence
$N_n(X_0)=\sum_jN_n(V_j)$ for every $n$ ([det-def-zeta]), and
$Z(X_0,T)=\prod_jZ(V_j,T)$. By the separated case each factor lies in
$\Q(T)\cap(1+T\Z[[T]])$, hence so does the product (integrality also follows
from [det-prop-euler]).

*Integral form.* [prop-weil-integral-rational-series] applied to
$Z(X_0,T)\in\Q(T)\cap(1+T\Z[[T]])$ gives coprime $A,B\in\Z[T]$ with
$A(0)=B(0)=1$ and $BZ=A$.
