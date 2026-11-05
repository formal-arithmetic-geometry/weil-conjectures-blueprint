+++
id = "lemma-flat-models-generators--1"
kind = "lemma"
title = "Flat models and generators (1)"
name_showing = false
order = 255001
aliases = ["bp-r075-1"]
lean = ["AlgebraicGeometry.Etale.hasTorAmplitudeIn_iff_exists_flatConstructibleModel", "AlgebraicGeometry.Etale.DerivedCategory.exists_flatConstructibleModel_of_boundedConstructibleFiniteTor"]
uses = ["definition-constructible-sheaves"]
+++
Let $X$ be a Noetherian scheme and $A$ a finite commutative ring. For
$C\in D^b_c(X_{\acute{e}t},A)$ and integers $a\leq b$, the following are
equivalent:

1. $C$ has Tor amplitude in $[a,b]$.
2. $C$ is represented by a complex $P$ of flat constructible $A$-sheaves
   on $X_{\acute{e}t}$ with $P^q=0$ for $q<a$ or $q>b$.

In particular, every $C\in D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$ has a bounded
flat constructible model.
