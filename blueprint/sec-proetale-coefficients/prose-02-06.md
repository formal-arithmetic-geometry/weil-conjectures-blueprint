+++
id = "prose-02-06"
kind = "hidden"
title = "Why w-contractible rings are needed"
order = 926
+++
To compute limits of sheaves by taking sections, we want objects over
which every cover splits, so that sheafification changes nothing there.
On the étale site the spectrum of a strictly henselian local ring
(a henselian local ring with separably closed residue field, such as the
étale local ring of a variety at a geometric point) has
this property, but such spectra do not cover $X$. The rings we need are
families of strictly henselian local rings over a profinite set of
components, with the extra condition that this set is
*extremally disconnected*: the closure of every open subset is
open. This condition is what lets us split a cover: over each
component of $\operatorname{Spec}(R)$ we choose a component of the cover
lying above it, and the choice can be made continuously. These rings, the w-contractible
rings, are defined below by a hierarchy of local conditions, and every
ring has a faithfully flat ind-étale cover by one of them
(Theorem [sk-thm-pe-wc-cover]).
