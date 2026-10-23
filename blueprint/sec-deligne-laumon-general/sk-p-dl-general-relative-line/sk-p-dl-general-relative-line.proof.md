+++
kind  = "proof"
of    = "sk-p-dl-general-relative-line"
+++
The assertion is immediate if $F=0$. Suppose that $F\ne0$, and fix a
closed point $y$ of $Y_0$. We first bound the stalks. Compact-support
base change ([sk-thm-sf-comp-composition], in the form
[sk-prop-sf-cbc]) identifies

$$
 (R^ih_!F)_{\bar y}=H_c^i(U_{\bar y},F)
$$

together with its local Frobenius operator. The restriction of $F$ to
the fibre is again pure of weight $w$, because a residue extension
raises both an eigenvalue and the residue cardinality to the same
power. After a finite extension of $\kappa(y)$, the nonempty
components of the fibre are geometrically connected smooth affine
curves, and [sk-cor-wft-curve-upper] bounds the weights of the
cohomology of each of them by $w+i$. Taking the direct sum and then
roots of the powers of the eigenvalues, we get the same bound over
$\kappa(y)$. In particular, $R^ih_!F=0$ outside degrees $1,2$.

Next we prove that $R^ih_!F$ is mixed, using the real envelope
([sk-prop-wrp-real-envelope]). Choose $b$ with
$|\iota(b)|=q^{-w/2}$, by taking a root of a nonzero local eigenvalue
as in that proposition, and let $B_b$ be the corresponding
geometrically constant twist. Put $F^0=F\otimes B_b$ and
$E=F^0\oplus(F^0)^\vee$; this is the real envelope of $F$, a lisse
sheaf that is real and pure of weight zero. At a closed point $y$
write

$$
 P_{i,y}(T)=\det(1-TF_y\mid H_c^i(U_{\bar y},E)).
$$

By [sk-l-dl-a1-endpoints], $P_{0,y}=1$ and every
reciprocal root of $P_{2,y}$ has modulus $q_y$, and by the bound just
proved every reciprocal root of $P_{1,y}$ has modulus at most
$q_y^{1/2}$. For a disconnected fibre these statements follow by the
same constant-extension argument.

By the Euler product and the determinant identity of
[sk-thm-trace-transport], after applying $\iota$ we have

$$
 L_\iota(U_y,E,T)=\frac{\iota P_{1,y}(T)}{\iota P_{2,y}(T)}.
$$

Since the Euler factors are real, this rational function has real
Taylor coefficients, and so it equals its complex conjugate as a
rational function, both being regular at zero. The numerator and the
denominator are coprime, because a common root would give an
eigenvalue having both permitted moduli, whereas $q_y^{1/2}<q_y$.
A reduced fraction whose numerator and denominator have constant
coefficient one is unique, and comparing it with its conjugate we
find $\iota P_{1,y},\iota P_{2,y}\in\mathbf R[T]$.
Therefore the sheaves $R^ih_!E$, which are constructible by the
finiteness theorems ([sk-thm-sf-ctf-stability]), are real at every
closed point, and [sk-i-dl-general-real] gives a finite mixed
filtration of each of them.

By additivity, $R^ih_!F^0$ is a direct summand of $R^ih_!E$, hence is
mixed. The projection formula for the constant twist identifies it
with $R^ih_!F\otimes B_b$, and untwisting shifts the weight of every
pure quotient by $w$ while preserving the finite Weil filtration.
It follows that $R^ih_!F$ is mixed. Finally, the bound on its stalks
proved above and [sk-lem-wgen-punctual-cutoff] show that every
nonzero quotient in this filtration has weight at most $w+i$.
