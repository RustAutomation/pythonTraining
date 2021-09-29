from pixellib.instance import instance_segmentation
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
def object_detection_on_an_image():
    segment_image = instance_segmentation()
    segment_image.load_model("C:\\Users\\Acer\\PycharmProjects\\pythonObjectValidate\\venv\\object\\mask_rcnn_coco.h5")

    target_class = segment_image.select_target_classes(person=True)

    result = segment_image.segmentImage(
        image_path="1city.jpg",
        # show_bboxes=True,
        segment_target_classes=target_class,
        # extract_segmented_objects=True,
        # save_extracted_objects=True,
        # output_image_name="outputV2.jpg"
    )

    objects_count = len(result[0]["scores"])
    print(f"{objects_count} Objects found")

def main():
    object_detection_on_an_image()

if __name__ == '__main__':
    main()