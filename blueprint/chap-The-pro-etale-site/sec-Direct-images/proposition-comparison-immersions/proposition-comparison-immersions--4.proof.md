+++
kind = "proof"
of = "proposition-comparison-immersions--4"
order = 139008
uses = ["proposition-comparison-immersions--2", "theorem-comparison-direct-images"]
+++
This is the informal deduction of the retained statement; the Lean
proof does not package or invoke this compactification comparison.

Write the factorization as $X\xrightarrow{j}\bar X\xrightarrow{\bar f}Y$.
The proper morphism $\bar f$ is quasi-compact and quasi-separated.
Apply [theorem-comparison-direct-images] to $\bar f$, precomposing
with $j_{\acute{e}t,!}$, and then apply
$R\bar f_{\mathrm{pro}\acute{e}t,*}$ to the isomorphism of
[proposition-comparison-immersions--2]. This gives

$$
\nu_Y^*R\bar f_{\acute{e}t,*}j_{\acute{e}t,!}
\simeq R\bar f_{\mathrm{pro}\acute{e}t,*}\nu_{\bar X}^*j_{\acute{e}t,!}
\simeq R\bar f_{\mathrm{pro}\acute{e}t,*}j_{\mathrm{pro}\acute{e}t,!}\nu_X^*.
$$

Exactness of extension by zero and comparison pullback, and boundedness
below of right derived direct images on bounded below complexes, give
the stated source and target categories.
