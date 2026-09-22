+++
id = "lem-sc-laurent-units"
kind = "lemma"
title = "Units of polynomial and Laurent polynomial rings"
order = 3912
lean = ["Polynomial.isUnit_iff_of_field", "LaurentPolynomial.isUnit_iff_of_field"]
+++
Let $k$ be a field.

- (a) The units of the polynomial ring $k[y_1,\dots,y_N]$ are the nonzero
  constants $k^\times$.
- (b) The units of the Laurent polynomial ring
  $k[T_1^{\pm1},\dots,T_d^{\pm1}]$ are the monomials
  $\lambda T_1^{m_1}\cdots T_d^{m_d}$ with $\lambda\in k^\times$ and
  $m_1,\dots,m_d\in\mathbf Z$.

## Proof

(a) If $uv=1$ with $u,v\neq0$, then $u$ and $v$ are nonzero and
$\deg(u)+\deg(v)=\deg(1)=0$, so $\deg u=0$ and $u$ is a nonzero constant.

(b) Let $u=\sum_{\mathbf n\in Z}a_{\mathbf n}T^{\mathbf n}$ and
$v=\sum_{\mathbf n\in W}b_{\mathbf n}T^{\mathbf n}$ be nonzero, with
finite supports $Z,W\subseteq\mathbf Z^d$ and all coefficients nonzero.
Choose $\mathbf c\in\mathbf Z^d$ such that
$\mathbf n\mapsto\mathbf c\cdot\mathbf n$ is injective on $Z\cup W$ (a
generic choice, finitely many differences being avoided), and put
$\ell(\mathbf n)=\mathbf c\cdot\mathbf n$. Let $\mathbf n_0\in Z$ be a
point where $\ell|_Z$ is maximal and $\mathbf n_1\in W$ a point where
$\ell|_W$ is maximal. If $\mathbf n+\mathbf n'=\mathbf n_0+\mathbf n_1$
with $\mathbf n\in Z$, $\mathbf n'\in W$, then
$\ell(\mathbf n)\leq\ell(\mathbf n_0)$ and
$\ell(\mathbf n')\leq\ell(\mathbf n_1)$ with equality of the sums, so both
are equalities and injectivity gives $\mathbf n=\mathbf n_0$,
$\mathbf n'=\mathbf n_1$. Hence the coefficient of
$T^{\mathbf n_0+\mathbf n_1}$ in $uv$ is
$a_{\mathbf n_0}b_{\mathbf n_1}\neq0$. If $uv=1$, this forces
$\mathbf n_0+\mathbf n_1=0$ and shows that $\ell$ is $\leq0$ on $Z+W$;
applying the same argument to the pair of minimisers gives $\ell\geq0$ on
$Z+W$, so $\ell=0$ on $Z+W$ and injectivity on $Z\cup W$ gives
$Z+W=\{0\}$. Thus $Z=\{\mathbf n_0\}$ and
$u=\lambda T^{\mathbf n_0}$ with $\lambda\neq0$, and
$\lambda\in k^\times$ because $uv=1$.
