+++
id = "proposition-compactness-finite-coefficients--1"
kind = "proposition"
title = "Compactness for finite coefficients (1)"
name_showing = false
order = 471001
aliases = ["bp-r143-1"]
lean = []
uses = ["definition-constructible-sheaves", "definition-localizing-subcategory"]
+++
This compactness and generation statement is bypassed by the current Lean proof
of the Weil conjectures and has no corresponding declaration in the mainline.
For finite coefficients, Lean constructs the exceptional inverse image using
Brown representability on the full étale derived category.

Every object of $D^b_{\mathrm{ctf}}(X,A)$ is compact in $\Loc(D^b_{\mathrm{ctf}}(X,A))$,
and a small skeleton of $D^b_{\mathrm{ctf}}(X,A)$ is a set of compact generators.
