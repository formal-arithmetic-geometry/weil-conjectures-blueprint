+++
kind = "proof"
of = "proposition-weights-under-usual-operations--16"
order = 1070017
uses = []
+++
Arithmetic Frobenius raises every $\ell$-power root of unity to the
$q$th power. Evaluating the cyclotomic character modulo each power of
$\ell$ therefore gives $q$; geometric Frobenius is its inverse.
Mapping the inverse cyclotomic unit to $\overline{\mathbf Q}_\ell$
gives $q^{-1}$. The definition of
`AlgebraicGeometry.WeilSheaf.tateTwistSheafNat` in degree one is the
constant sheaf twisted by this unit. Its local Frobenius is its
$\deg(x)$th power, by
`AlgebraicGeometry.WeilSheaf.constantTwist_adicConstant_stalk_frobenius`.
