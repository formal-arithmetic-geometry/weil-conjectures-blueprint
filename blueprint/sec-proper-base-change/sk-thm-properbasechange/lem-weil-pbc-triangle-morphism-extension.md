+++
id = "lem-weil-pbc-triangle-morphism-extension"
kind = "lemma"
title = "Extending a morphism of the middle terms to distinguished triangles; uniqueness when Hom(X[1],Z')=0"
uses = ["def-weil-triangulated-category", "def-weil-pbc-triangles-with-shift"]
tags = ["stacks-0146"]
+++
Let $\mathcal T$ be a pre-triangulated category [def-weil-triangulated-category] and let $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{d}X[1 ]$ and $X'\xrightarrow{u'}Y'\xrightarrow{v'}Z'\xrightarrow{d'}X'[1 ]$ be distinguished triangles, and $g:Y\to Y'$ a morphism. (1) The following are equivalent: (a) $v'gu=0$; (b) there is $f:X\to X'$ with $u'f=gu$; (b') there is $h:Z\to Z'$ with $hv=v'g$; (c) there are $f,h$ such that $(f,g,h)$ is a morphism of triangles. (2) If moreover $\Hom_{\mathcal T}(X[1 ],Z')=0$, then the $f$ of (b) and the $h$ of (b') are unique; consequently, for any $f$ with $u'f=gu$ and any $h$ with $hv=v'g$, $(f,g,h)$ is a morphism of triangles, i.e. also $d'h=f[1 ]d$. (3) In particular, if $\Hom_{\mathcal T}(X[1 ],Z)=0$, then $d$ is the unique morphism $x:Z\to X[1 ]$ such that $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{x}X[1 ]$ is distinguished.
