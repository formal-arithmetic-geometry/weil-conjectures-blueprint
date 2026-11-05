+++
kind = "proof"
of = "lemma-change-coefficients-direct-image--3"
order = 635007
uses = ["lemma-inverse-image-coefficient-sheaves"]
+++
Choose an $E$-basis $b_1,\ldots,b_r$ of $F$. Its constant global sections identify $F_X$ with $E_X^r$, as in [lemma-inverse-image-coefficient-sheaves]. Extension of scalars is exact, and, after restriction to $E$, the maps $K\to K_F$ obtained by multiplying the scalar-extension unit by the $b_i$ identify $K_F$ with $K^r$ in the unbounded derived category.

Derived pushforward is linear in these constant sections and commutes with finite sums. The mate of the comparison under extension and restriction of scalars is the canonical isomorphism expressing commutation of restriction of scalars with $Rf_*$. Together with the basis identifications, this identifies the comparison itself with the finite-sum comparison and proves it is an isomorphism.

The same basis argument on sheaves identifies the underived comparison with $(f_*M)^r\to f_*(M^r)$. For an injective $E_X$-module $I$, the underlying abelian sheaf of $F_X\otimes_{E_X}I$ is injective, since it is a finite sum of copies of the injective underlying sheaf of $I$. These facts also supply the finite-stage inputs for passage to algebraic-closure coefficients.
