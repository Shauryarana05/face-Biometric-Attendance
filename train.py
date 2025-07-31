from src.config import TrainConfig
from src.train_main import TrainMain
import argparse
import torch

if __name__ == "__main__":
    # Parse command-line arguments
    p = argparse.ArgumentParser(description="Training Face-AntiSpoofing Model")
    p.add_argument("--crop_dir", type=str, default='data128', 
                   help="Subdir with cropped images")
    p.add_argument("--input_size", type=int, default=128, 
                   help="Input size of images passed to model")
    p.add_argument("--batch_size", type=int, default=256, 
                   help="Count of images in the batch")
    p.add_argument("--num_classes", type=int, default=2, choices=[2, 3],
                   help="2 for binary or 3 for live-print-replay classification")
    p.add_argument("--job_name", type=str, default='job', 
                   help="Suffix for model name saved in snapshots dir")
    args = p.parse_args()

    # Define spoof category setup
    if args.num_classes == 2:
        spoof_categories = 'binary'
    elif args.num_classes == 3:
        spoof_categories = [[0], [1, 2, 3], [7, 8, 9]]

    # Select device (GPU if available)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    # Initialize configuration with device
    cnf = TrainConfig(
        crop_dir=args.crop_dir,
        input_size=args.input_size,
        batch_size=args.batch_size,
        spoof_categories=spoof_categories,
        device=device   # pass device explicitly
    )

    cnf.set_job(args.job_name)

    # Start training
    trainer = TrainMain(cnf)
    trainer.train_model()
    print('Training Finished.')
