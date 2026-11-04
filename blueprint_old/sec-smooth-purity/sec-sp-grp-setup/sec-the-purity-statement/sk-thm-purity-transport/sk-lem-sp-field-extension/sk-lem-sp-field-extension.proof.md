+++
kind = "proof"
of = "sk-lem-sp-field-extension"
uses = ["sk-lem-sp-reduction", "sk-prop-sp-integral-adjunction"]
+++
Since $\mathcal O_F$ is finite free over $\mathcal O_E$, $-\otimes\mathcal O_{F,T}$
commutes with $R\varprojlim$ and reduces at level $n$ to extension along
$\mathcal O_E/\ell^n\to\mathcal O_F/\ell^n$. There [sk-lem-sp-reduction] gives the
comparisons with their compatibilities with units, counits, purity maps and
composition; they commute with the reductions $n\to m$ by the composition
statement, so they are maps of the towers defining $Rf_{!,\mathcal O_E}$ and
$H_{f,\mathcal O_E}$ of [sk-prop-sp-integral-adjunction]. Apply $R\varprojlim$ and
invert $\ell$.
