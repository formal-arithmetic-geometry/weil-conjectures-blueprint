+++
kind = "proof"
of = "lemma-twisted-envelope--1"
order = 1277002
uses = ["lemma-artin-schreier-character-sheaf", "proposition-extension-zero-restriction-closed-subscheme", "definition-real-sheaves"]
+++
For a Weil sheaf $F$, write
$T_n(F,x)=\iota\operatorname{Tr}(\operatorname{Frob}_x^n\mid F_{\bar x})$.
At a closed point $x\in U_0$ of degree $d$, the eigenvalues of
$M^\dagger$ are $b^d\alpha^{-1}$, where $\alpha$ runs through those of
$M$. Purity and $\iota(b)=q^w$ give

$$
\iota(b^d\alpha^{-1})
=\frac{q^{dw}}{\iota(\alpha)}
=\overline{\iota(\alpha)}.
$$

Consequently $T_n(M^\dagger,x)=\overline{T_n(M,x)}$ for every
$n\ge0$. The stalks of an extension by zero agree with the original
stalks on the open and vanish off it, as in
[proposition-extension-zero-restriction-closed-subscheme]. Thus on the
whole affine line,

$$
T_n(j_!M^\dagger,x)=\overline{T_n(j_!M,x)}.
$$

Now fix a closed point $z$ of the Fourier square and put $x=p_1(z)$.
The rank-one Frobenius calculation for the Artin--Schreier sheaf
[lemma-artin-schreier-character-sheaf], together with the stalk formulas
for pullback and tensor product, gives $c\in k_0$ and $r,e\in\mathbf N$
such that

$$
T_n(\mathcal K_\psi\otimes p_1^*j_!M,z)
=\iota(\psi(c))^{rn}T_{en}(j_!M,x).
$$

The same $c,r,e$ work for $\psi^{-1}$ and $M^\dagger$. The character
values have finite order, so
$\iota(\psi(c)^{-1})=\overline{\iota(\psi(c))}$, and the traces of
every Frobenius power on the two summands are complex conjugate.
Their sum is therefore real. The trace criterion for reality, obtained
from the Newton identities, shows that the local polynomial of their
direct sum has real coefficients, as required by
[definition-real-sheaves].
