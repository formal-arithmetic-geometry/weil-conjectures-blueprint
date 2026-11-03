+++
id = "prose-01-04"
kind = "hidden"
title = "Counting points in families"
order = 9
+++
The proofs of Weil's axioms do not proceed one variety at a time, and
neither does counting points. If $Z_0\subset X_0$ is
closed with complement $U_0$, then
$\#X_0(\mathbf F_q)=\#U_0(\mathbf F_q)+\#Z_0(\mathbf F_q)$. If
$f:X_0\to Y_0$ is a morphism, then

$$
\#X_0(\mathbf F_q)=\sum_{y\in Y_0(\mathbf F_q)}\#f^{-1}(y)(\mathbf F_q),
$$

a sum over the base of a function that is not constant. The proof of
purity goes further. After shrinking, a variety is fibred in curves over
a variety of one dimension less, and the essential case is a sheaf on a
curve, where the bound comes from a positivity argument and the Fourier
transform; along the way one pulls functions back, multiplies them and
takes their Fourier transforms.

For cohomology to follow these manipulations, functions have to be
replaced by sheaves. This is Grothendieck's dictionary between functions
and sheaves [sga4-5, Sommes trig.]. A constructible complex $K$ on
$X$ with a Frobenius structure (a Weil complex,
Section [sec-frobenius]) has a *trace function*
$t_K:X_0(\mathbf F_{q^m})\to\Ql$, whose value at $x$ is the trace of
Frobenius on the stalk $K_{\bar x}$. The operations on functions are
matched by operations on sheaves:

| on functions | on sheaves | in these notes |
|---|---|---|
| $t\mapsto t\circ f$ | $f^*K$ | Part “The six operations” |
| $t\cdot t'$ | $K\otimes^{\mathbf L}K'$ | Part “The six operations” |
| $t\mapsto\bigl(y\mapsto\sum_{f(x)=y}t(x)\bigr)$ | $Rf_!K$ | Corollary [sk-cor-tf-trace-function-pushforward] |
| $t=t|_U+t|_Z$ | $j_!j^*K\to K\to i_*i^*K\to$ | Part “The six operations” |
| $t\mapsto\bigl(y\mapsto-\sum_xt(x)\psi(xy)\bigr)$ | $Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1]$ | Section [sec-fourier-transform] |
| $\sum_{x\in X_0(\mathbf F_{q^m})}t(x)$ | $R\Gamma_c(X,K)$ | Section [sec-trace-formula] |

The last line is the trace formula, and the third is its relative form:
the trace function of $Rf_!K$ is the sum of $t_K$ over the fibres. Since
$Rf_!$ of a sheaf is a complex, all of this takes place in a derived
category, where traces are additive in distinguished triangles. In the
table, $\psi$ is a nontrivial additive character of $\mathbf F_q$,
replaced by $\psi\circ\operatorname{Tr}_{\mathbf F_{q^m}/\mathbf F_q}$
over $\mathbf F_{q^m}$, and $\mathcal K_\psi$ is the Artin–Schreier
sheaf on $\mathbf A^1\times\mathbf A^1$ with trace function $\psi(xy)$.

Duality has no such simple counterpart on functions, but it is the other
half of the proof: it gives axiom (c), and it turns an upper bound for
weights into purity. It needs the two remaining operations, internal
$\cHom$ and the exceptional inverse image $f^!$. Together with $Rf_*$, these are the *six operations* $f^*$, $Rf_*$, $Rf_!$, $f^!$,
$\otimes^{\mathbf L}$ and $\cHom$. Part “The six operations” constructs
them, with the base change theorems relating them, for $\ell$-adic
coefficients.
