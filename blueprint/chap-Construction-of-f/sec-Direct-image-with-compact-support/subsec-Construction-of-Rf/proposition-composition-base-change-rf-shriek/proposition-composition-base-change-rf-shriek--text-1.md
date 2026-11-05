+++
id = "proposition-composition-base-change-rf-shriek--text-1"
kind = "hidden"
title = "Composition and base change for $Rf_!$"
order = 516001
uses = ["definition-constructible-sheaves", "proposition-construction-independence-rf-shriek"]
+++
*Shared context for the formalized details.* Fix a prime $\ell$ and a field
$k$ of characteristic $p>0$, with $p\ne\ell$. Except in the explicitly stated
finite-coefficient variants, all schemes are separated and of finite type over
$k$, and all morphisms are $k$-morphisms. Work on
$\Dbc(-_{\mathrm{pro}\acute{e}t},\Lambda)$ with the condensed coefficient rings
associated to $\Lambda=\Qbarl$, a finite extension $E\subset\Qbarl$ of $\Ql$,
or its ring of integers $\Oe$, as specified in each statement.
The coherence statements below concern $\Qbarl$-coefficients. These are the
bounded constructible categories of the Lean declarations; the details do not
assert an extension to $\Loc(\Dctf)$ for every admissible coefficient ring.
