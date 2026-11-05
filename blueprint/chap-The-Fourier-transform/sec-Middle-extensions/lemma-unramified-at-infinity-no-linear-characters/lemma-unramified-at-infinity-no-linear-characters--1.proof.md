+++
kind = "proof"
of = "lemma-unramified-at-infinity-no-linear-characters--1"
order = 1267002
uses = ["lemma-artin-schreier-character-sheaf", "proposition-topos-functoriality", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-pro-etale-refinements-weakly-etale"]
+++
For the first assertion, multiplication by zero factors through the
Artin–Schreier map, along which the character sheaf becomes constant.
Thus $\mathcal L_{\psi(0x)}|_U\simeq\overline{\mathbf Q}_\ell$.
The geometric open $U$ is irreducible. Apply the sheaf-theoretic Clifford
argument, `AlgebraicGeometry.WeilSheaf.IsIrreducibleLisse.exists_iso_biproduct_unit`:
choose an irreducible lisse subsheaf of $M|_U$ and take the sums of its
successive Frobenius translates. Their ranks are bounded, so the sums
stabilize. The stable sum has a Weil structure and is nonzero, hence is
all of $M|_U$ by irreducibility. A trivial constituent of this sum must
occur in one of the irreducible translates. Frobenius pullback preserves
the constant sheaf, so all the translates are constant, and their lisse
quotient $M|_U$ is a finite direct sum of constant rank-one sheaves.

For the second assertion, write $t=1/x$ and put $K=\bar k_0((t))$.
The point $x=1/t$ lifts to $U$ and extends across infinity to the formal
disc $\operatorname{Spec}\bar k_0\llbracket t\rrbracket$. Pull back a lisse
extension of $M$ to this disc. Its ring is strictly henselian, hence
w-contractible by [proposition-w-local-components]. A member of a
trivializing pro-étale cover meeting the closed point has a section, by
[theorem-pro-etale-refinements-weakly-etale] and
[proposition-splitting-ind-etale-covers]. Pulling the trivialization back
along this section shows that the sheaf on the disc is constant. Its
restriction to $\operatorname{Spec}K$ is therefore constant as well; this
is `AlgebraicGeometry.WeilSheaf.exists_iso_upperStar_biproduct_unit_of_isUnramifiedAtInfinity`.

Suppose that $\mathcal L_{\psi(ax)}|_U$, with $a\ne0$, were a geometric
constituent of $M$. Exact pullback to $\operatorname{Spec}K$ would make
$\mathcal L_{\psi(a/t)}$ a quotient of a subsheaf of a constant sheaf.
Put $q=\#k_0$. In an algebraic closure of $K$, choose a root of
$u^q-u=a/t$. Every translation $u\mapsto u+c$, $c\in k_0$, is induced
by a $K$-automorphism of this algebraic closure. On the Artin–Schreier
trivialization of the character sheaf, this translation acts by
$\psi(-c)$. Choose $c$ for which $\psi(-c)\ne1$. A quotient of a
subsheaf of a constant sheaf cannot have this action, giving the
contradiction formalized by
`AlgebraicGeometry.affineLine.not_epi_upperStar_laurentPoint_artinSchreierImage`.
This argument uses neither irreducibility nor semisimplicity of $M$.
