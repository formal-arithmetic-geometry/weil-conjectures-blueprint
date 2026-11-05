+++
kind = "proof"
of = "proposition-weights-under-usual-operations--10"
order = 1070011
uses = ["definition-weights"]
+++
For a closed point $z$ of $X_0$, put $x=f(z)$ and
$r=[\kappa(z):\kappa(x)]$. The degrees satisfy
$\deg(z)=r\deg(x)$, with $r>0$. The stalk comparison identifies the
characteristic polynomial of Frobenius on $(f^*\mathcal F)_{\bar z}$
with that of $\operatorname{Frob}_x^r$ on $\mathcal F_{\bar x}$.
Lean uses `AlgebraicGeometry.WeilSheaf.charpoly_frobeniusEnd_stalkAt_of_dvd`
and `FrobeniusModule.IsPureOfWeight.of_charpoly_eq_pow`. Since
$q_z=q_x^r$, raising the eigenvalues to the $r$th power preserves
the normalized weight $w$.
