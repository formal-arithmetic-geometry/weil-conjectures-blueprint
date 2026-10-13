+++
id = "prop-a1-curve-perverse-simples"
kind = "theorem"
tags = ["latex:proposition"]
title = "Simple perverse sheaves on a smooth curve"
order = 3092
uses = ["def-wf-middle-extension", "lem-weil-heart-short-exact-triangles", "lem-wf-dense-open-pi1-surjective", "thm-a1-curve-perverse-heart"]
+++
In the setting and with the conventions of [thm-a1-curve-perverse-heart],
the simple objects of the abelian category $\mathrm{Perv}(C)$ are the
following:

- the *punctual* objects $i_{x*}E$ (in degree $0$), where $x$ is a closed
  point of $C$ and $E$ is an irreducible sheaf on $x$, that is, an
  irreducible Weil module at $x$ in the Weil case;
- the *middle extensions* $(j_*\mathcal N)[1]$ of [def-wf-middle-extension],
  where $j:U\hookrightarrow C$ is a dense open immersion and $\mathcal N$
  is a nonzero irreducible lisse sheaf on $U$. Here irreducible means that
  $\mathcal N$ has no lisse subsheaf other than $0$ and $\mathcal N$.

Every object of either kind is simple, and every simple object is of one
of these kinds.
