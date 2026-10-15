+++
id = "sk-def-pe-wlocal"
kind = "definition"
title = "The local hierarchy"
order = 705
tags = ["sketch"]
+++
A spectral space $T$ is *w-local* if its set $T^c$ of closed points is closed and every
point specializes to exactly one closed point. A ring $R$ is w-local if
$\operatorname{Spec}(R)$ is w-local. It is *w-strictly local* if it is w-local and
$R_{\mathfrak m}$ is strictly henselian for every maximal ideal $\mathfrak m$. It is
*w-contractible* if it is w-strictly local and the profinite space
$\pi_0(\operatorname{Spec}(R))$ is extremally disconnected.

Recall that spectral spaces are quasi-compact and sober, with a basis of quasi-compact
opens closed under finite intersections. The space of connected components of a spectral
space is profinite. For a w-local space the natural map $T^c\to\pi_0(T)$ is a
homeomorphism: each component consists of the generalizations of its unique closed point,
and $T^c$ is compact. For $T=\operatorname{Spec}(R)$ this component is the image of
$\operatorname{Spec}(R_{\mathfrak m})$. Thus w-strict locality gives strictly henselian
geometry component by component, and w-contractibility also controls how choices vary
across the profinite set of components. Closedness of $T^c$ is a separate condition: it
does not follow from uniqueness of closed specializations. See Stacks, Tags 096A, 0968
and 0969.
