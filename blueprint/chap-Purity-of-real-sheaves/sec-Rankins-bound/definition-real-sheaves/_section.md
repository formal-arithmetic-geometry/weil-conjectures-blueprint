+++
id = "definition-real-sheaves"
kind = "definition"
title = "Real sheaves"
order = 1153
lean = ["AlgebraicGeometry.WeilSheaf.IsReal", "AlgebraicGeometry.WeilGroup.IsReal"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local"]
+++
A Weil sheaf $\mathcal G$ is $\iota$-real if
$\iota\det(1-T\operatorname{Frob}_x\mid\mathcal G_{\bar x})$ has real coefficients for
every closed point; equivalently, the multiset of its complex
eigenvalues at each point is stable under complex conjugation.  In
particular, the traces of all positive powers of local Frobenius are
real.
