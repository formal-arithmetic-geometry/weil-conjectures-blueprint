+++
id = "prose-02-07"
kind = "hidden"
title = "w-local and w-contractible rings (1)"
order = 42
+++
To compute limits of sheaves by taking sections, we want objects over
which every cover splits, so that sheafification changes nothing there.
On the étale site the spectrum of a strictly henselian local ring,
such as the étale local ring of a variety at a geometric point, has
this property, but such spectra do not cover $X$. Instead, the rings we need are
families of strictly henselian local rings over a profinite set of
components. Moreover, we require this set to be extremally disconnected, which means
that the closure of every open subset is open, because under this condition a cover
splits. Namely, over each component of $\operatorname{Spec}(R)$ we choose a
component of the cover lying above it, and extremal disconnectedness lets us
make this choice continuously. The model case is the ring of locally
constant functions from a profinite set to a separably closed field
(Example [example-locally-constant-functions-w-local]), which is a family
of copies of one field indexed by the profinite set. Below we define these
rings, the w-contractible rings, by a hierarchy of local conditions, and we show that every
ring has a faithfully flat ind-étale cover by one of them
(Theorem [theorem-existence-contractible-covers]).

Recall that spectral spaces are quasi-compact and sober, with a basis
of quasi-compact opens closed under finite intersections, and that the space of
connected components of a spectral space is profinite.
