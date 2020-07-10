var merge = function (nums1, m, nums2, n) {
  for (let i = 0; i < n; i++) {
    nums1[m + i] = nums2[i];
  }

  return nums1.sort((a, b) => a - b);
};

var merge = function (nums1, m, nums2, n) {
  let length = m + n;
  m--;
  n--;

  while (length--) {
    if (n < 0 || nums1[m] > nums2[n]) {
      nums1[length] = nums1[m--];
    } else {
      nums1[length] = nums2[n--];
    }
  }
  return nums1;
};
